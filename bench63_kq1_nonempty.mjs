// bench63 — K-Q1 非空 graph query 計測: transact (datom 投入) 後の認証付き query n=30 + 3 warmup
// bench62_kq1_n30.mjs に transact ステップを追加 (bench49_kq1_warmquery2.mjs の txEdn 形式)。
// secret は一切記録せず鍵は zero-fill。
import { randomBytes } from "node:crypto";
import { secp256k1 } from "@noble/curves/secp256k1.js";
import { keccak_256 } from "@noble/hashes/sha3.js";

const AUTHN = "https://auth.kotobase.net";
const API = "https://kotobase.net";
const RETURN_TO = "https://kotobase.net/admin";
const WARMUP = 3, N = 30;

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
  const ms = performance.now() - t0;
  let data;
  try { data = JSON.parse(text); } catch { data = { raw: text.slice(0, 512) }; }
  return { response, data, ms };
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
function percentile(sorted, p) { // nearest-rank
  const idx = Math.ceil((p / 100) * sorted.length) - 1;
  return sorted[Math.max(0, Math.min(sorted.length - 1, idx))];
}

const privateKey = randomBytes(32);
const publicKey = secp256k1.getPublicKey(privateKey, false);
const address = `0x${hex(keccak_256(publicKey.slice(1))).slice(-40)}`;
const runId = `kvstats-nonempty-${Date.now()}`;

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

  // transact: datom 投入 (bench49 形式)
  const txEdn = `[{ :db/id "${runId}" :bench/run-id "${runId}" :bench/value "authenticated" }]`;
  const write = await timedFetch(`${API}/xrpc/ai.gftd.apps.kotobase.datomic.transact`, {
    method: "POST", headers: xrpcHeaders,
    body: JSON.stringify({ db_name: runId, tx_edn: txEdn }),
  });
  const writeStatus = write.response.status;
  const writeBody = JSON.stringify(write.data).slice(0, 300);
  if (writeStatus !== 200) {
    console.log(JSON.stringify({
      purpose: "bench63 K-Q1 non-empty graph query (KV read breakdown)",
      observedAt: new Date().toISOString(), runId,
      transactStatus: writeStatus, transactBody: writeBody,
      result: "transact failed — measured run aborted (no fabricated data)",
    }, null, 2));
    process.exit(0);
  }

  const queryEdn = `{:find [?e ?value] :where [[?e :bench/run-id "${runId}"] [?e :bench/value ?value]]}`;

  const warmup = [];
  const measured = [];
  for (let i = 0; i < WARMUP + N; i += 1) {
    const q = await timedFetch(`${API}/xrpc/ai.gftd.apps.kotobase.datomic.q`, {
      method: "POST", headers: xrpcHeaders,
      body: JSON.stringify({ graph, db_name: runId, query_edn: queryEdn }),
    });
    const rec = {
      i, status: q.response.status, ms: Math.round(q.ms * 100) / 100,
      kvStats: q.response.headers.get("x-kotobase-kv-stats"),
      rows: Array.isArray(q.data) ? q.data.length
        : (Array.isArray(q.data?.rows) ? q.data.rows.length : undefined),
    };
    if (q.response.status !== 200) rec.body = JSON.stringify(q.data).slice(0, 200);
    if (i < WARMUP) warmup.push(rec); else measured.push(rec);
  }

  const ok = measured.filter((r) => r.status === 200);
  const lat = ok.map((r) => r.ms).sort((a, b) => a - b);
  const headerObserved = measured.filter((r) => r.kvStats !== null && r.kvStats !== undefined).length;
  const kvValues = [...new Set(measured.map((r) => r.kvStats).filter((v) => v != null))];
  console.log(JSON.stringify({
    purpose: "bench63 K-Q1 non-empty graph query KV read breakdown (n=30 + 3 warmup, bench49 method)",
    observedAt: new Date().toISOString(),
    runId,
    transactStatus: writeStatus,
    warmup,
    summary: {
      n: measured.length, ok200: ok.length,
      headerObserved, headerObservedCount: `${headerObserved}/30`,
      kvStatsValues: kvValues,
      p50: percentile(lat, 50), p95: percentile(lat, 95), p99: percentile(lat, 99),
      min: lat[0] ?? null, max: lat[lat.length - 1] ?? null,
      sampleRows: measured.find((r) => r.rows !== undefined)?.rows,
    },
    measured,
  }, null, 2));
} finally {
  privateKey.fill(0);
}
