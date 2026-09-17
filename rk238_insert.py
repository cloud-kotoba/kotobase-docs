import io, sys

PATH = "query-cosientist.md"
HDR = "## Iteration log"

with io.open(PATH, "r", encoding="utf-8") as f:
    wt = f.read()

if wt.count(HDR) != 1:
    print("FATAL: header count=%d" % wt.count(HDR)); sys.exit(1)

idx = wt.index(HDR) + len(HDR)
if not wt.startswith("\n", idx):
    print("FATAL: no newline after header"); sys.exit(1)
idx += 1

rest = wt[idx:]
if not rest.startswith("- 2026-09-09: bench 第245回。09:28 JST tick。"):
    print("FATAL: first entry is not bench245"); sys.exit(1)

entry = (
"- 2026-09-09: rank 第239回。09:35 JST tick。HEAD df710a7 = bench 第245回 "
"(09:28, K-Z3 9時台 run540 cold 4/60 ~6.7%) = remote bench_fetch/main・net-kotobase/main 一致 "
"(git fetch + rev-parse 比較乖離 0; detached HEAD のため fetch 系で取込, terminal foreground stdout 空=既知のため状態確認・計測出力はファイル書出経由)。"
"pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 帯 artifact) — "
"true progressive NEXT は iter-log HEAD 連鎖 (bench 第245回 NEXT「委ねる (rank 指定優先; フォールバックは "
"K-Z3 現在時刻帯 9時台 n 積み増し続行, 次 run ID は run541 使用)」)。"
"rank 第238回 (09:06) 以降の新規確定 evidence は 3 commits (falsify 第239回 run538 帯初 0/60, bench 第244回 run539 帯初 0/60, "
"bench 第245回 run540 4/60 — 本 tick 冒頭 run538 は worktree uncommitted 滞留で orphaned 疑いとしたが、直後に falsify/bench が commit (a482611, df710a7) し解消、"
"my insert は abort 済みで未反映。全て 9時台 K-Z3 測定)。取り込み判定: (a) K-Z3: 3 commits を 9時台通算に積上げ、"
"9時台 (9/9) 通算 = falsify run538 (0/60) + bench run539 (0/60) + bench run540 (4/60 ~6.7%, "
"run540A 散発 2/20 + run540B 散発 2/20 + run540C 0/20 即消失, control 0/20 完全静穏分離成立) = 4/180 (~2.2%) の 3 セット。"
"帯初 0/60 完全静穏 2 連 (run538+run539) → run540 散発 4/60 弱再上振れ で朝帯静穏低位帯候補方向を弱く継続、"
"K-Z3 traffic 依存説への強反証材料なし (9時台帯初 n=2 完全静穏 + 3 セット 4/180 ~2.2% は 5時台 5/180 ~2.8% と同水準の低位帯)。"
"但し帯 n=3 で帯水準確定・機構判断には未達 (K-Z3 open 継続, fallback 専門のまま)。"
"(b) K-Q1: 変動なし — transact 401 動的照合が唯一の残る切れ手で cosientist 実装専任・rank 測定指示対象外, KV read 内訳初実測滞留継続, 最上位維持。"
"(c) K-Z2/K-S1/K-S2: evidence なし (変動なし)。"
"status 遷移なし (transition 要件を満たす判定的 evidence なし — K-Z3 は open 継続・9時台 3 セット 4/180 ~2.2% で帯水準確定・機構判断とも未達, "
"run540 散発 4/60 は帯内即消失 + 帯 n=3 で確定に不足; K-Q1 は cosientist 実装専任, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (確認済み勝ち仮説なし)。"
"rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 9時台 3 セット ~2.2% は朝帯静穏低位帯候補方向で優先度逆転なし)。"
"live smoke 200 (/, /signup; pre-run monitor 計測 200)。host load1 ~19-22 (09:28-09:35 uptime 実測, gate 7.5 大幅超過) — "
"rank は測定せず状態正本の更新のみで影響なし。secret は一切記録せず。"
"NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 9時台 n 積み増し継続, 次 run ID は run541 使用 — "
"run538/539/540 消費済みのため次セットは run541)。\n"
)

new_wt = wt[:idx] + entry + wt[idx:]

with io.open(PATH, "w", encoding="utf-8") as f:
    f.write(new_wt)

# verify
with io.open(PATH, "r", encoding="utf-8") as f:
    v = f.read()
if v.count(HDR) != 1:
    print("VERIFY FAIL: header count=%d" % v.count(HDR)); sys.exit(1)
ri = v.find("rank 第239回")
bi = v.find("- 2026-09-09: bench 第245回")  # should be the ORIGINAL first entry, now second
hi = v.find(HDR) + len(HDR)
order_ok = hi < ri < bi
print("VERIFY: header=1 rank239_present=%s bench245_second=%s order_ok=%s" % (ri>=0, bi>=0, order_ok))
if not (ri>=0 and bi>=0 and order_ok):
    sys.exit(1)
print("INSERT_DONE")