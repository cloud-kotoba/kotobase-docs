import fs from "node:fs";
const path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md";
const lines = fs.readFileSync(path, "utf8").split("\n");
// K-Q1 行は 3 行構成: テーブル行 (starts "| K-Q1") + 続き行 2 行。テーブル行を探す。
const idx = lines.findIndex((l) => l.startsWith("| K-Q1"));
if (idx < 0) throw new Error("K-Q1 row not found");
const add = " cosientist 2026-09-06 (第82回, rank 第80回 NEXT 切れ手(a)「delegation-for-request の graph/tenant binding 実装照合 (CID 再束縛文字列 vs mint 時名前文字列の不一致)」をコード実査 + 固定入力 parity 計算で反証試行, ネットワークなし, secret 不含): (1) mint 側 authn/worker.cljs:1856-1860 は cid/canonical-graph(tenant-did, (str/trim db-name)) で graph スコープを埋め込む。 (2) gateway proxy.cljc:958-975 bind-tenant-write-graph は graph-cid-from-name(\"kotobase/db/\" did \"/\" (trim db_name)) で再束縛 — trim 前提が mint と同一。 (3) engine xrpc.cljs:1327-1335 write-graph-name は kotobase.cid/canonical-graph(iss, (str/trim db-name)) — gateway が body.graph を付けても upstream は iss+db_name から再導出し client CID は使わない (xrpc.cljs:38 の設計注記どおり)。 (4) 三式のバイト列 parity を固定入力 (did + db_name 3 パターン, trim 有無含む) で node 実測 (_cosient82_cid_parity.mjs): mint/gateway/engine の同一式は同一 CID を生む (trim あり式は 3 パターン全一致, trim なし混入時のみ不一致 — 三者とも trim するため不成立)。 結論: CID 再束縛 vs 名前束縛の不一致説は棄却 (反証成立) — 401 の残る切れ手は (i) authority_from_model の scope 照合 (verify-biscuit-action に渡る graph 引数が canonical CID に対し mint スコープが kotoba://graph/<名前文字列> という「scope リソース文字列 vs 要求 graph 文字列」の不一致 — authority_from_model は resources に kotoba://graph/<graph 引数そのまま> を要求するため graph 引数が CID なら mint 時の名前スコープと不一致になり得る: 次の反証対象), (ii) cacao_b64 経路への harness 変更, の 2 本に再収束。 status 判定は rank に委ねる (cosientist はコード変更なし)。";
lines[idx] = lines[idx].replace(/\s*$/, "") + add;
fs.writeFileSync(path, lines.join("\n"));
console.log("appended at line " + (idx + 1) + ", new len=" + lines[idx].length);
