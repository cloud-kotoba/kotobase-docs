import fs from "node:fs";
const path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md";
const lines = fs.readFileSync(path, "utf8").split("\n");
const idx = lines.findIndex((l) => l.startsWith("| K-Q1"));
if (idx < 0) throw new Error("K-Q1 row not found");
const add = " cosientist 2026-09-06 (第82回続, 切れ手(i)「authority_from_model の scope 照合不一致」を同一 tick 内で反証試行, ネットワークなし, secret 不含): 鎖のコード実査 — (1) authn mint (worker.cljs:1856-1860) は :graph = cid/canonical-graph(tenant-did, trim(dbName)) つまり mint スコースは既に kotoba://graph/<canonical CID> (名前文字列ではない), (2) engine handle-transact (xrpc.cljs:2049) は expected-graph = write-graph-name(tenant, db-name) = 同一 canonical CID, (3) authority_from_model の graph_resource = \"kotoba://graph/\" + graph 引数 (= CID)。固定入力実測 (_cosient82_scope_parity.mjs): mintScope == graphResource (同一 CID 文字列, match=true)。 結論: scope リソース文字列の不一致説も静的には棄却材料 — mint/verify とも同一 canonical CID 式で parity 成立。残る 401 起源は wire 検証そのもの (biscuit.wire decode/ed25519 verify 失敗 → auth.cljs:307-310 の catch で 401 に畳まれる経路) か tenant-did 形状 (engine tenant-did-re は did:web 多段を許容, 一見整合) の実 token 依存要因で、静的照合では切り分け不能 — 反証には (ii) cacao_b64 経路への harness 変更 または wire verifier の local 単体再現が必要。status 判定は rank に委ねる。";
lines[idx] = lines[idx].replace(/\s*$/, "") + add;
fs.writeFileSync(path, lines.join("\n"));
console.log("appended, new len=" + lines[idx].length);
