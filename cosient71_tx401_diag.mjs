// cosient71 — transact 401 write path 診断 (bench62 flow 再使用, ephemeral EOA, secret 不含, 鍵 zero-fill)。
// 測定: (1) transact の status/body (401 なら details で分岐特定), (2) 同一 Biscuit の getSession (authn 再検証),
// (3) transact 直前の認証付き query (200 対比), (4) Biscuit ヘッダ長 (形状確認, token 値は記録しない)。
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
const runId = `cosient71-tx-${Date.now()}`;
const steps = [];

try {
  const options = await timedFetch(`${AUTHN}/v1/siwe/options`, {
    method: "POST", headers: jsonHeaders(),
    body: JSON.stringify({ address, chain_id: "1", return_to: RETURN_TO }),
  });
  steps.push({ step: "siwe_options", status: options.response.status });

  const signature = signatureFor(options.data.message, privateKey);
  const verification = await timedFetch(`${AUTHN}/v1/siwe/verify`, {
    method: "POST", headers: jsonHeaders(),
    body: JSON.stringify({ nonce: options.data.nonce, signature }),
  });
  steps.push({ step: "siwe_verify", status: verification.response.status, valid: verification.data?.valid });
  const cookie = cookieFrom(verification.response);

  const created = await timedFetch(`${AUTHN}/v1/tenants`, {
    method: "POST", headers: jsonHeaders({ cookie }),
    body: JSON.stringify({ name: `cosient71 txdiag ${runId}` }),
  });
  steps.push({ step: "tenant_provision", status: created.response.status, tenantIdPresent: created.data?.tenant?.id != null });
  const tenantId = created.data.tenant?.id;
  const tenantDid = created.data.tenant?.did;

  const issued = await timedFetch(`${AUTHN}/v1/biscuit/token`, {
    method: "POST", headers: jsonHeaders({ cookie }),
    body: JSON.stringify({ tenantId, dbName: runId, permissions: ["data:read", "data:write"] }),
  });
  steps.push({
    step: "biscuit_issue", status: issued.response.status,
    authorizationPresent: issued.data?.authorization != null,
    authScheme: typeof issued.data?.authorization === "string" ? issued.data.authorization.split(" ", 1)[0] : null,
    authLen: typeof issued.data?.authorization === "string" ? issued.data.authorization.length : null,
    graphPresent: issued.data?.graph != null,
  });
  const authorization = issued.data.authorization;
  const graph = issued.data.graph;

  const xrpcHeaders = { "content-type": "application/json", authorization,
    "x-kotobase-tenant-did": tenantDid, "x-kotobase-db-name": runId };

  // (3) 認証付き read 対比 (空 graph)
  const preQuery = await timedFetch(`${API}/xrpc/ai.gftd.apps.kotobase.datomic.q`, {
    method: "POST", headers: xrpcHeaders,
    body: JSON.stringify({ graph, db_name: runId, query_edn: "{:find [?e] :where [[?e :db/ident ?e]]}" }),
  });
  steps.push({ step: "pre_transact_query", status: preQuery.response.status, ms: preQuery.ms,
    body: JSON.stringify(preQuery.data).slice(0, 200) });

  // (1) transact 本体 — 401 の details をそのまま記録
  const txEdn = `[{ :db/id "${runId}" :cosient71/run-id "${runId}" :cosient71/value "probe" }]`;
  const write = await timedFetch(`${API}/xrpc/ai.gftd.apps.kotobase.datomic.transact`, {
    method: "POST", headers: xrpcHeaders,
    body: JSON.stringify({ db_name: runId, tx_edn: txEdn }),
  });
  steps.push({ step: "transact", status: write.response.status, ms: write.ms,
    body: JSON.stringify(write.data).slice(0, 500) });

  // (2) 同一 Biscuit の authn 再検証 (viewer の permissions を確認)
  const sess = await timedFetch(`${API}/xrpc/com.atproto.server.getSession`, {
    method: "POST", headers: xrpcHeaders, body: "{}",
  });
  const perms = sess.data?.permissions ?? sess.data?.did ? undefined : undefined;
  steps.push({ step: "getSession_same_biscuit", status: sess.response.status, ms: sess.ms,
    bodyKeys: sess.data && typeof sess.data === "object" ? Object.keys(sess.data).slice(0, 12) : null,
    body: JSON.stringify(sess.data).slice(0, 500) });

  console.log(JSON.stringify({
    purpose: "cosient71 transact 401 write path diagnostic (bench62 flow, ephemeral EOA, no secrets recorded)",
    observedAt: new Date().toISOString(), runId, steps,
  }, null, 2));
} finally {
  privateKey.fill(0);
}
