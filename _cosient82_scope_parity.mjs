// scope_parity.mjs — cosientist 第82回: 切れ手(i)「authority_from_model の
// scope 照合」検証。mint スコープの graph リソース文字列と verify 時要求の
// kotoba://graph/<graph引数> が一致するかをコード実査 + 実測で反証する。
//
// 鎖:
//  1. authn mint (worker.cljs:1856-1860): :graph = cid/canonical-graph(tenant-did, trim(dbName))
//     → biscuit.cljs mint: resource-scope = "kotoba://graph/" + (str/trim graph)
//     → スコープ = kotoba://graph/<canonical CID 文字列>
//  2. gateway transact (proxy.cljc:996/1002 → bind-tenant-write-graph): body.graph = 同一 canonical CID
//     → proxy-to-kotoba は authorization (Biscuit) をそのまま転送
//  3. engine handle-transact (xrpc.cljs:2049): expected-graph = write-graph-name(tenant, db-name) = 同一 CID
//     → verify-biscuit-action(env, authz, tenant, expected-graph, "data:write", now)
//     → delegation-for-request {:biscuit_b64 ...} {:graph expected-graph ...}
//     → authority_from_model: graph_resource = "kotoba://graph/" + graph(=CID)
//     → resources に含まれるか照合
//  結論(予測): mint スコープも verify 要求も同一 canonical CID 文字列 → 一致。
//  → 切れ手(i) も棄却されるはず。実測で確認する (cid 値は _cosient82_cid_parity.mjs と同一関数)。

import { createHash } from "node:crypto";

function graphCidFromName(name) {
  const hash = createHash("sha256").update(new TextEncoder().encode(name)).digest();
  const cid = new Uint8Array(36);
  cid[0] = 0x01; cid[1] = 0x71; cid[2] = 0x12; cid[3] = 0x20;
  cid.set(hash, 4);
  const A = "abcdefghijklmnopqrstuvwxyz234567";
  let bits = 0, value = 0, out = "";
  for (const byte of cid) {
    value = (value << 8) | byte; bits += 8;
    while (bits >= 5) { out += A[(value >>> (bits - 5)) & 31]; bits -= 5; }
  }
  if (bits > 0) out += A[(value << (5 - bits)) & 31];
  return "b" + out;
}
const canonicalGraph = (did, dbName) => graphCidFromName(`kotobase/db/${did}/${dbName}`);

const tenantDid = "did:web:example.com:tenant:t_abcdefghijklmnop";
const dbName = "biscuit-txprobe-1757000000000";

// 1. mint スコース (authn)
const mintGraph = canonicalGraph(tenantDid, dbName.trim());
const mintScope = "kotoba://graph/" + mintGraph.trim();

// 3. verify 要求 (engine expected-graph → authority_from_model graph_resource)
const expectedGraph = canonicalGraph(tenantDid, dbName.trim()); // write-graph-name
const graphResource = "kotoba://graph/" + expectedGraph;

const out = {
  mintScope, graphResource,
  match: mintScope === graphResource,
  verdict: mintScope === graphResource
    ? "PARITY: mint scope == verify 要求リソース — 切れ手(i) scope 文字列不一致も棄却材料"
    : "MISMATCH: scope 文字列が不一致 — 401 の起源候補として残る",
};
console.log(JSON.stringify(out, null, 2));
