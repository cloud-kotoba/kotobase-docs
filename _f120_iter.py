import io
P = "query-cosientist.md"
txt = io.open(P, encoding="utf-8").read()
ANCHOR = u"## Iteration log\n"
ITER = (u"- 2026-09-06: falsify 第120回。23:31 JST tick。worktree detached HEAD (HEAD 3170099 = bench 第106回 run262, fetch net-kotobase + rev-parse 比較で net-kotobase/main 先端一致確認)。live smoke 200 (/, /signup; pre-run 計測)。host load1 37.64 (23:31 uptime 実測, gate 7.5 大幅超過) のため local 測定は拒否し production HTTP フォールバック (gate 外)。rank 第114回 NEXT「K-Z3 23時台 n 積み増し継続...次 run ID は run262 使用」に従い 現在時刻帯 23時台 n 積み増しを実施 — ただし測定開始前に bench 第106回 (23:22) が run262 を先行 commit 済みのため、本測は run263 に読替 (run216/run256 前例で 23時台内の独立 2 計測, 本測 23:31): K-Z3 run263A–C (同測定法 n=20 × 3 + landing control, 別接続 curl, 23:31:22–23:31:51 JST, 全 80/80 200, 正 endpoint search.kotobase.net/search?q=test): cold(>=0.5s) 5/0/0 per 20 = 5/60 (~8.3%) — run263A cold 5/20 (1.2288/1.5429/1.2907/1.1089/1.1414s, 冒頭散発 3 件 + 中盤 2 件, warm 群と交互) p50 76.5ms / run263B 0/20 p50 54.0ms / run263C 0/20 p50 54.6ms, control (kotobase.net/signup) cold 0/20 p50 72.3ms 静穏で control 分離成立、cold 群は search 側に局在。run263A cold 5/20 は B/C 0/20 で即消失し 23時台 5 セット連続 cold>0 (run260 8/60 → run259 4/60 → run261 3/60 → run262 2/60 → 本 tick 5/60, 重→減弱→再上振れ) で K-Z3 traffic 依存説への反証材料継続 (車夜帯 ~26-31% 平坦パターンと整合方向)、23時台通算 22/300 (~7.3%)。帯区分算入可否・status 判定は rank に委ねる (rank 専門)。secret は一切記録せず (curl のみ + 統計 python ファイル)。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 23時台 n 積み増し続行)。\n")
assert ANCHOR in txt, "iter-log anchor not found"
fixed = txt.replace(ANCHOR, ANCHOR + ITER, 1)
io.open(P, "w", encoding="utf-8").write(fixed)
print("iter-log inserted")
print("falsify 第120回 occurrences:", fixed.count(u"falsify 第120回"))