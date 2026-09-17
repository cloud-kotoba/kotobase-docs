// cid_parity.mjs — cosientist 第82回: gateway/authn vs engine の graph CID 導出が
// 同一バイト列を生むかを固定入力で照合 (secret 不含, ネットワークなし)。
// authn (cid/canonical-graph): sha256("kotobase/db/" + did + "/" + db_name)
// gateway (graph-cid-from-name): 同一式, trim 差異のみ
// 判定対象: db_name の trim 差 ("pins " vs "pins") が CID を変えるか、
// did が header 経路 (caller-did trim) と mint 経路 (context :tenant-did) で一致するか。

import { createHash } from "node:crypto";

function graphCidFromName(name) {
  const hash = createHash("sha256").update(new TextEncoder().encode(name)).digest();
  const cid = new Uint8Array(36);
  cid[0] = 0x01; cid[1] = 0x71; cid[2] = 0x12; cid[3] = 0x20;
  cid.set(hash, 4);
  const ALPHABET = "abcdefghijklmnopqrstuvwxyz234567";
  let bits = 0, value = 0, out = "";
  for (const byte of cid) {
    value = (value << 8) | byte; bits += 8;
    while (bits >= 5) { out += ALPHABET[(value >>> (bits - 5)) & 31]; bits -= 5; }
  }
  if (bits > 0) out += ALPHABET[(value << (5 - bits)) & 31];
  return "b" + out;
}
const canonicalGraph = (did, dbName) => graphCidFromName(`kotobase/db/${did}/${dbName}`);

const did = "did:web:example.com:tenant:t_abcdefghijklmnop";
const cases = [
  ["plain", "pins", "pins"],
  ["trim-mismatch", "pins", "pins "],
  ["spaces-around", "bench/run", "  bench/run"],
];
const out = { cases: [], verdict: null };
for (const [label, mintDbName, gatewayDbName] of cases) {
  const authnCid = canonicalGraph(did, mintDbName);          // mint 時 (trim なし連結)
  const gatewayCid = canonicalGraph(did, gatewayDbName.trim()); // bind-tenant-write-graph (trim 後連結)
  out.cases.push({ label, authnCid, gatewayCid, equal: authnCid === gatewayCid });
}
// mint 側 worker.cljs は cid/canonical-graph(tenant-did, (str/trim db-name)) —
// つまり trim 後連結。上の authnCid は trim しない場合の差分も見る。
const untrimmed = canonicalGraph(did, "pins ");
out.untrimmedVsTrimmed = { untrimmed, trimmed: canonicalGraph(did, "pins"), equal: untrimmed === canonicalGraph(did, "pins") };
out.verdict = out.cases.every((c) => c.equal) && out.untrimmedVsTrimmed.equal
  ? "PARITY: trim 後の式は完全一致 — CID 導出の不一致は 401 の起源ではない"
  : "MISMATCH DETECTED";
console.log(JSON.stringify(out, null, 2));
