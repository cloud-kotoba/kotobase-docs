# cosientist run497: append to K-Z3 evidence cell (line 279, 1-indexed) + insert iter-log line after header
PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

kz3_append = (" cosientist 2026-09-08 (K-Z3 19時台帯 3 セット目 run497A-C — falsify 第221回 run496 直後の独立 n 積み増し, "
 "NEXT 継続 → 現在時刻帯 19時台, 次 run ID run497, 同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, "
 "nearest-rank p50, 正 endpoint search.kotobase.net/search?q=test + control kotobase.net/signup, "
 "19:45:21-19:45:44 JST, 全 80/80 200, host load1 34.89 (19:41 uptime, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, "
 "secret 不含 — curl + python stats のみ): cold(>=0.5s) 2/1/0 per 20 = 3/60 (~5.0%) — "
 "run497A 散発 2/20 (1.1342s/1.7329s) p50 0.1433s / run497B 単発 1/20 (0.9598s) p50 0.0790s / "
 "run497C 0/20 p50 0.0645s — landing control (kotobase.net/signup) cold 0/20 p50 0.0946s max 0.3061s 完全静穏で "
 "control 分離成立、cold 群は search 側に局在。run497A 散発 2 件 + B 単発は C 0/20 + control 0/20 で即消失し "
 "「帯内 1 窓即消失」散発型継続 (run496A 散発クラスタ 4/20 の 11 分後弱い再出現, heavy>=6/20 は非再現継続)。"
 "19時台 (9/8) 通算 = bench run495 (0/60) + falsify run496 (5/60) + 本測 run497 (3/60) = 8/180 (~4.4%) の 3 セットで "
 "18時台 (27/300 ~9.0%) より低位の中間帯候補、日中帯短時間スケール変動と整合で traffic 依存説の日中帯方向支持継続、"
 "深夜帯 ~26-31% 平坦パターンとの対比不変。status 判定は rank に委ねる (rank 専門)")

iter_line = ("- 2026-09-08: cosientist 第149回。19:43 JST tick。HEAD 6cfacff = falsify 第221回 (19:36, K-Z3 19時台 "
 "run496 cold 5/60 ~8.3%) = remote net-kotobase/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため "
 "fetch 系で取込; terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書き出し経由; pre-run monitor NEXT"
 "「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 第90回帯 artifact) — true progressive NEXT は "
 "iter-log HEAD 連鎖 (falsify 第221回 委ねる → フォールバック K-Z3 現在時刻帯 19時台 n 積み増し, 次 run ID は run497))。"
 "qualify する新 evidence は 0 本 (K-Q1 は残余 cosientist 実装専任の動的照合のみ・測定で qualify する実装改善なし — "
 "反証が先規律でコード変更なし; K-Z2/K-Z3 は観測継続, K-S1/K-S2 は evidence なし) のため観測 tick。live smoke 200 "
 "(/, /signup; pre-run 計測)。host load1 34.89 (19:41 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外で実施。"
 "K-Z3 19時台 run497A-C 実測 (同測定法): cold(>=0.5s) 3/60 (~5.0%) — run497A 散発 2/20 (1.1342s/1.7329s) / "
 "run497B 単発 1/20 (0.9598s) / run497C 0/20, control 0/20 完全静穏で control 分離成立、cold 群 search 側局在。"
 "19時台 (9/8) 通算 8/180 (~4.4%) 3 セット。status 判定は rank に委ねる (rank 専門)。secret は一切記録せず。"
 "詳細は K-Z3 evidence 欄 (L279 末尾) に追記。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 19時台 n 積み増し続行, "
 "次 run ID は run498 使用)。")

with open(PATH, "r", encoding="utf-8") as f:
    lines = f.readlines()

# 1) append to K-Z3 evidence cell line 279 (index 278)
idx = 278
if idx < len(lines) and lines[idx].rstrip("\n").startswith("| K-Z3 |"):
    # cell content ends before newline; append kz3_append
    lines[idx] = lines[idx].rstrip("\n") + kz3_append + "\n"
    print("K-Z3 cell appended at line", idx+1)
else:
    raise SystemExit("ERROR: line 279 is not K-Z3 cell")

# 2) insert iter-log line after "## Iteration log" header
header_idx = None
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        header_idx = i
        break
if header_idx is None:
    raise SystemExit("ERROR: '## Iteration log' header not found")
lines.insert(header_idx + 1, iter_line + "\n")
print("iter-log inserted after line", header_idx + 1)

with open(PATH, "w", encoding="utf-8") as f:
    f.writelines(lines)
print("DONE")