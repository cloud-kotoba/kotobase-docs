import { randomBytes } from "node:crypto";
import { secp256k1 } from "@noble/curves/secp256k1.js";
import { keccak_256 } from "@noble/hashes/sha3.js";

// Follow-up to cosient81 probe: A/B 401 vs C/D 400 with same headers implies
// the 401 is not basic authn but something on the tx_edn write path.
// Probe: add x-kotobase-ref (issuer-bound graph ref) / x-datomic-db-name
// headers as the F-probe error message suggests.

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
  const started = performance.now();
  const response = await fetch(url, init);
  const text = await response.text();
  const durationMs = performance.now() - started;
  let data;
  try { data = JSON.parse(text); } catch { data = { raw: text.slice(0, 512) }; }
  return { response, data, durationMs };
}
function describe(label, result) {
  return { label, status: result.response.status,
    body: JSON.stringify(result.data).slice(0, 300), ms: Math.round(result.durationMs) };
}
function cookieFrom(response) {
  const value = response.headers.getSetCookie?.()[0] || response.headers.get("set-cookie");
  if (!value) throw new Error("no session cookie");
  return value.split(";", 1)[0];
}

const privateKey = randomBytes(32);
const publicKey = secp256k1.getPublicKey(privateKey, false);
const address = `0x${hex(keccak_256(publicKey.slice(1))).slice(-40)}`;
const runId = `biscuit-txprobe2-${Date.now()}`;
const out = { runId, observedAt: new Date().toISOString(), probes: [] };

try {
  const options = await timedFetch(`${AUTHN}/v1/siwe/options`, {
    method: "POST", headers: jsonHeaders(),
    body: JSON.stringify({ address, chain_id: "1", return_to: RETURN_TO }),
  });
  if (options.response.status !== 200) throw new Error(`siwe options ${options.response.status}`);
  const signature = signatureFor(options.data.message, privateKey);
  const verification = await timedFetch(`${AUTHN}/v1/siwe/verify`, {
    method: "POST", headers: jsonHeaders(),
    body: JSON.stringify({ nonce: options.data.nonce, signature }),
  });
  if (verification.response.status !== 200 || verification.data.valid !== true)
    throw new Error("SIWE did not validate");
  const cookie = cookieFrom(verification.response);

  const created = await timedFetch(`${AUTHN}/v1/tenants`, {
    method: "POST", headers: jsonHeaders({ cookie }),
    body: JSON.stringify({ name: `Biscuit tx probe2 ${runId}` }),
  });
  if (created.response.status !== 201) throw new Error(`provision ${created.response.status}`);
  const tenantId = created.data.tenant?.id;
  const tenantDid = created.data.tenant?.did;

  const issued = await timedFetch(`${AUTHN}/v1/biscuit/token`, {
    method: "POST", headers: jsonHeaders({ cookie }),
    body: JSON.stringify({ tenantId, dbName: runId, permissions: ["data:read", "data:write"] }),
  });
  if (issued.response.status !== 201) throw new Error(`issuance ${issued.response.status}`);
  const authorization = issued.data.authorization;
  const graph = issued.data.graph;

  const base = { "content-type": "application/json", authorization,
    "x-kotobase-tenant-did": tenantDid, "x-kotobase-db-name": runId };
  const txEdn = `[{ :db/id "${runId}" :bench/run-id "${runId}" :bench/value "v2" }]`;
  const body = JSON.stringify({ graph, db_name: runId, tx_edn: txEdn });
  const T = `${API}/xrpc/ai.gftd.apps.kotobase.datomic.transact`;

  // G: add x-kotobase-ref bound to the issued graph CID.
  const g = await timedFetch(T, { method: "POST",
    headers: { ...base, "x-kotobase-ref": graph }, body });
  out.probes.push(describe("G(with x-kotobase-ref)", g));

  // H: add x-datomic-db-name header too.
  const h = await timedFetch(T, { method: "POST",
    headers: { ...base, "x-datomic-db-name": runId }, body });
  out.probes.push(describe("H(with x-datomic-db-name)", h));

  // I: both ref + db-name headers.
  const i = await timedFetch(T, { method: "POST",
    headers: { ...base, "x-kotobase-ref": graph, "x-datomic-db-name": runId }, body });
  out.probes.push(describe("I(ref+dbname)", i));

  // J: graph as "ref" body field instead of graph.
  const j = await timedFetch(T, { method: "POST", headers: base,
    body: JSON.stringify({ ref: graph, db_name: runId, tx_edn: txEdn }) });
  out.probes.push(describe("J(ref-body)", j));

  out.summary = out.probes.map((p) => `${p.label}: ${p.status}`);
} finally {
  privateKey.fill(0);
}
process.stdout.write(`${JSON.stringify(out, null, 2)}\n`);
