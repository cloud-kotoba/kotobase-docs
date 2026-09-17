// bench65 — transact 401 独立調査事項の診断 (ステップ別 status 記録, 新規 ephemeral EOA 1 回のみ)
// bench63_kq1_nonempty.mjs と同一 flow で各ステップの status/body を記録。secret は記録せず鍵は zero-fill。
import { randomBytes } from "node:crypto";
import { secp256k1 } from "@noble/curves/secp256k1.js";
import { keccak_256 } from "@noble/hashes/sha3.js";

const AUTHN = "https://auth.kotobase.net";
const API = "https://kotobase.net";
const RETURN_TO = "https://kotobase.net/admin";

function hex(b) { return Buffer.from(b).toString("hex"); }
function eip191Digest(message) {
  const payload = Buffer.from(message, "utf8");
  const prefix = Buffer.from(`\x19Ethereum Signed Message:\n${payload.length}`, "utf8");
  return keccak_256(Buffer.concat([prefix, payload]));
}
function jsonHeaders(extra = {}) {
  return { "content-type": "application/json", origin: AUTHN, ...extra };
}
function signatureFor(message, privateKey) {
  const recovered = secp256k1.sign(eip191Digest(message), privateKey, {
    prehash: false, lowS: true, format: "recovered",
  });
  const signature = new Uint8Array(65);
  signature.set(recovered.slice(1), 0);
  signature[64] = 27 + recovered[0];
  return `0x${hex(signature)}`;
}
async function timedFetch(url, init = {}) {
  const t0 = performance.now();
  const response = await fetch(url, init);
  const text = await response.text();
  const ms = Math.round((performance.now() - t0) * 100) / 100;
  let data;
  try { data = JSON.parse(text); } catch { data = { raw: text.slice(0, 512) }; }
  return { response, data, ms };
}
function cookieFrom(response) {
  const value = response.headers.getSetCookie?.()[0] || response.headers.get("set-cookie");
  return value ? value.split(";", 1)[0] : null;
}

const privateKey = randomBytes(32);
const publicKey = secp256k1.getPublicKey(privateKey, false);
const address = `0x${hex(keccak_256(publicKey.slice(1))).slice(-40)}`;
const runId = `kvstats-diag-${Date.now()}`;
const steps = [];

try {
  const options = await timedFetch(`${AUTHN}/v1/siwe/options`, {
    method: "POST", headers: jsonHeaders(),
    body: JSON.stringify({ address, chain_id: "1", return_to: RETURN_TO }),
  });
  steps.push({ step: "siwe_options", status: options.response.status, ms: options.ms });

  const signature = signatureFor(options.data.message, privateKey);
  const verification = await timedFetch(`${AUTHN}/v1/siwe/verify`, {
    method: "POST", headers: jsonHeaders(),
    body: JSON.stringify({ nonce: options.data.nonce, signature }),
  });
  steps.push({ step: "siwe_verify", status: verification.response.status, valid: verification.data?.valid, ms: verification.ms });
  const cookie = cookieFrom(verification.response);

  const created = await timedFetch(`${AUTHN}/v1/tenants`, {
    method: "POST", headers: jsonHeaders({ cookie }),
    body: JSON.stringify({ name: `kvstats diag ${runId}` }),
  });
  steps.push({ step: "tenant_provision", status: created.response.status, tenantIdPresent: created.data?.tenant?.id != null, ms: created.ms });
  const tenantId = created.data.tenant?.id;
  const tenantDid = created.data.tenant?.did;

  const issued = await timedFetch(`${AUTHN}/v1/biscuit/token`, {
    method: "POST", headers: jsonHeaders({ cookie }),
    body: JSON.stringify({ tenantId, dbName: runId, permissions: ["data:read", "data:write"] }),
  });
  steps.push({ step: "biscuit_issue", status: issued.response.status, authorizationPresent: issued.data?.authorization != null, graphPresent: issued.data?.graph != null, ms: issued.ms });
  const authorization = issued.data.authorization;
  const graph = issued.data.graph;

  const xrpcHeaders = { "content-type": "application/json", authorization,
    "x-kotobase-tenant-did": tenantDid, "x-kotobase-db-name": runId };

  // 認証付き read (query) を transact 前に 1 回 — 空グラフでも authz が通るかの対比
  const preQuery = await timedFetch(`${API}/xrpc/ai.gftd.apps.kotobase.datomic.q`, {
    method: "POST", headers: xrpcHeaders,
    body: JSON.stringify({ graph, db_name: runId, query_edn: "{:find [?e] :where [[?e :db/ident ?e]]}" }),
  });
  steps.push({ step: "pre_transact_query", status: preQuery.response.status, ms: preQuery.ms, body: JSON.stringify(preQuery.data).slice(0, 200) });

  const txEdn = `[{ :db/id "${runId}" :bench/run-id "${runId}" :bench/value "diag" }]`;
  const write = await timedFetch(`${API}/xrpc/ai.gftd.apps.kotobase.datomic.transact`, {
    method: "POST", headers: xrpcHeaders,
    body: JSON.stringify({ db_name: runId, tx_edn: txEdn }),
  });
  steps.push({ step: "transact", status: write.response.status, ms: write.ms, body: JSON.stringify(write.data).slice(0, 300) });

  console.log(JSON.stringify({
    purpose: "bench65 transact 401 diagnostic (step statuses, fresh ephemeral EOA, no fabricated data)",
    observedAt: new Date().toISOString(), runId, steps,
  }, null, 2));
} finally {
  privateKey.fill(0);
}
