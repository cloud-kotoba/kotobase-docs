// bench49 (第49回) — K-Q1 PR#3 (c3c508f) merge 後 production deploy 判別再試行
// bench49_reprobe と同じだが /signup smoke 後の再確認 + cosineist deploy 完了待ちで
// 繰り返し確認する 3 リクエスト probe。
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
  const response = await fetch(url, init);
  const text = await response.text();
  let data;
  try { data = JSON.parse(text); } catch { data = { raw: text.slice(0, 512) }; }
  return { response, data };
}
function requireStatus(label, result, expected) {
  if (result.response.status !== expected) {
    throw new Error(`${label}: HTTP ${result.response.status} ${JSON.stringify(result.data)}`);
  }
  return result;
}
function cookieFrom(response) {
  const value = response.headers.getSetCookie?.()[0] || response.headers.get("set-cookie");
  if (!value) throw new Error("SIWE verification did not issue a session cookie");
  return value.split(";", 1)[0];
}

const privateKey = randomBytes(32);
const publicKey = secp256k1.getPublicKey(privateKey, false);
const address = `0x${hex(keccak_256(publicKey.slice(1))).slice(-40)}`;
const runId = `kvstats-probe-${Date.now()}`;

try {
  const options = requireStatus("SIWE options",
    await timedFetch(`${AUTHN}/v1/siwe/options`, {
      method: "POST", headers: jsonHeaders(),
      body: JSON.stringify({ address, chain_id: "1", return_to: RETURN_TO }),
    }), 200);
  const signature = signatureFor(options.data.message, privateKey);
  const verification = requireStatus("SIWE verification",
    await timedFetch(`${AUTHN}/v1/siwe/verify`, {
      method: "POST", headers: jsonHeaders(),
      body: JSON.stringify({ nonce: options.data.nonce, signature }),
    }), 200);
  if (verification.data.valid !== true) throw new Error("SIWE did not validate");
  const cookie = cookieFrom(verification.response);

  const created = requireStatus("tenant provision",
    await timedFetch(`${AUTHN}/v1/tenants`, {
      method: "POST", headers: jsonHeaders({ cookie }),
      body: JSON.stringify({ name: `kvstats probe ${runId}` }),
    }), 201);
  const tenantId = created.data.tenant?.id;
  const tenantDid = created.data.tenant?.did;

  const issued = requireStatus("Biscuit issuance",
    await timedFetch(`${AUTHN}/v1/biscuit/token`, {
      method: "POST", headers: jsonHeaders({ cookie }),
      body: JSON.stringify({ tenantId, dbName: runId, permissions: ["data:read", "data:write"] }),
    }), 201);
  const authorization = issued.data.authorization;
  const graph = issued.data.graph;

  const xrpcHeaders = { "content-type": "application/json", authorization,
    "x-kotobase-tenant-did": tenantDid, "x-kotobase-db-name": runId };

  const queryEdn = `{:find [?e ?value] :where [[?e :bench/run-id "${runId}"] [?e :bench/value ?value]]}`;
  const results = [];
  for (let i = 0; i < 3; i += 1) {
    const q = await timedFetch(`${API}/xrpc/ai.gftd.apps.kotobase.datomic.q`, {
      method: "POST", headers: xrpcHeaders,
      body: JSON.stringify({ graph, db_name: runId, query_edn: queryEdn }),
    });
    if (q.response.status !== 200) {
      throw new Error(`query ${i}: HTTP ${q.response.status} ${JSON.stringify(q.data)}`);
    }
    results.push({
      status: q.response.status,
      kvStats: q.response.headers.get("x-kotobase-kv-stats"),
    });
  }
  const kvStats = results.map((r) => r.kvStats);
  console.log(JSON.stringify({
    purpose: "bench49 deploy re-probe round 2 (x-kotobase-kv-stats header presence x3)",
    observedAt: new Date().toISOString(),
    results,
    deployed: kvStats.every((v) => v !== null && v !== undefined),
  }, null, 2));
} finally {
  privateKey.fill(0);
}
