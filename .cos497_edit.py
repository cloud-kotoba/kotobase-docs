# cosientist run497 evidence append to K-Z3 cell (line 279, 1-indexed) + iter-log insert
import sys, io

PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

kz3_append = (" cosientist 2026-09-08 (K-Z3 19時台帯 3 セット目の独立 n 実測 run497A-C "
 "(falsify 第221回 run496 直後 19:45 JST, NEXT 継続指示 → 現在時刻帯 19時台 n 積み増し, 次 run ID run497), "
 "同測定法 n=20 x 3 + landing control, 別接続 curl, cold>=0.5s, nearest-rank p50, "
 "正 endpoint search.kotobase.net/search?q=test + control kotobase.net/signup, 19:45:21-19:45:44 JST, "
 "全 80/80 200, host load1 34.89-65.44 (19:41 uptime, gate 7.5 大幅超過) は production HTTP 実測のため gate 外, "
 "secret 不含 — curl + python stats のみ): cold(>=0.5s) 2/1/0 per 20 = 3/60 (~5.0%) — "
 "run497A 散発 2/20 (1.1342s/1.7329s) p50 0.1433s / run497B 単発 1/20 (0.9598s) p50 0.0790s / "
 "run497C 0/20 p50 0.0645s - landing control (kotobase.net/signup) 0/20 p50 0.0946s max 0.3061s 完全静穏で "
 "control 分離成立、cold 群は search 側に局在。run497A 散発 2 件 + B 単発は C 0/20 + control 0/20 で即消失し "
 "「帯内 1 窓即消失」散発型継続 (run496A 散発クラスタ 4/20 の 11 分後弱い再出現, heavy>=6/20 は run493 以降非再現継続)。"
 "19時台 (9/8) 通算 = bench run495 (0/60) + falsify run496 (5/60) + 本測 run497 (3/60) = 8/180 (~4.4%) の 3 セット "
 "で 18時台 (27/300 ~9.0%) より低位の中間帯候補、日中帯短時間スケール変動と整合で traffic 依存説の日中帯方向支持継続、"
 "深夜帯 ~26-31% 平坦パターンとの対比不変。status 判定は rank に委ねる (rank 専門)")

iter_line = ("- 2026-09-08: cosientist 第149回。19:43 JST tick。HEAD 6cfacff = falsify 第221回 (19:36, K-Z3 19時台 run496 cold 5/60 ~8.3%) = remote bench_fetch/main・net-kotobase/main 一致 … run497。live smoke 200 (/, /signup; pre-run 計測)。host load1 34.89-65.44 (19:41 uptime 実測, gate 7.5 大幅超過) は production HTTP 実測のため gate 外。※pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 第90回帯 artifact, 前例多) — true progressive NEXT は iter-log HEAD 連鎖 (falsify 第221回 「委ねる → フォールバック K-Z3 現在時刻帯 n 積み増し, 次 run ID は run497」)。qualify する新 evidence は 0 本 (K-Q1 残余は cosientist 実装専任の動的照合のみ, 反証が先で測定 の qualify なし — コード変更なし; K-Z2/K-Z3 は観測継続, 19-21/K-S1/K-S2 は evidence なし) のため観測 tick。K497 (同測定法, 19:45 JST): 3/60 ~5.0%, cold 群 search 側 ・control 0/20 完全静穏 separation 成立。19時台 5/120→8/180。詳細は K-Z3 evidence 欄 (末尾) 追記。secret は一切記録せず。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 19時台 n 積み増し続行 次 19:56 前後, 次 run ID は run498 使用)。")

"""
NOTE: THE ABOVE PLACEHOLDER FOR iter_line IS UNSTABLE FOR THE CANONICAL — rebuilding below."""