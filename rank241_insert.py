#!/usr/bin/env python3
import io, sys

path = 'query-cosientist.md'
d = open(path, encoding='utf-8').read()

entry = (
"- 2026-09-09: rank 第241回。10:10 JST tick。HEAD 78c6404 = falsify 第241回 (10:00 commit, "
"K-Z3 9時台 run543 cold 3/60 ~5.0% = control 0/20 完全静穏分離成立) = remote bench_fetch/main・net-kotobase/main 一致 "
"(git fetch + rev-parse 比較乖離 0; detached HEAD のため fetch 系で取込, worktree diff HEAD -- query-cosientist.md 空 + "
"HDR_COUNT=1 事前確認; terminal foreground stdout 空=既知のため状態確認はファイル書出経由)。pre-run monitor NEXT"
"「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 帯 artifact) — true progressive NEXT は iter-log "
"HEAD 連鎖 (falsify 第241回 NEXT「委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 9時台 n 積み増し続行, "
"次 run ID は run544 使用 — run538..543 消費済み)」)。rank 第240回 (09:51) 以降の新規確定 evidence は 1 commit のみ — "
"falsify 第241回 run543 (10:00 commit, 09:52-53 計測, K-Z3 9時台 6 セット目): cold(>=0.5s) 0/1/2 per 20 = 3/60 (~5.0%), "
"run543B 単発 1.0597s pos1 冒頭 + run543C 散発 2/20 冒頭集中 (1.0099s/1.1510s), control 0/20 p50 0.1321s max 0.2808s 完全静穏で "
"control 分離成立, cold 群 search 側局在, heavy>=6/20 非再現継続。取り込み判定: (a) K-Z3: run543 を 9時台通算に積上げ、"
"9時台 (9/9) 通算 = run538 (0/60) + run539 (0/60) + run540 (4/60) + run541 (0/60) + run542 (1/60) + run543 (3/60) = 8/360 "
"(~2.2%) の 6 セット — 朝帯静穏低位帯候補方向を 6 セット連続で維持 (5時台 ~2.8% と同水準, K-Z3 traffic 依存説への強反証材料なし)。"
"帯水準は 6 セットで朝帯低位帯として概ね確定方向だが機構判断には未達 (K-Z3 open 継続, fallback 専門のまま)。"
"(b) K-Q1: 変動なし — transact 401 動的照合が唯一の残る切れ手で cosientist 実装専任・rank 測定指示対象外, KV read 内訳初実測滞留継続, "
"最上位維持。(c) K-Z2/K-S1/K-S2: evidence なし (変動なし)。status 遷移なし (transition 要件を満たす判定的 evidence なし — "
"K-Z3 は open 継続・9時台 6 セット ~2.2% で帯水準は概ね確定方向だが機構判断に未達; K-Q1 は cosientist 実装専任, "
"K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (確認済み勝ち仮説なし)。rank 順位変動なし "
"(K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 9時台 6 セット ~2.2% は朝帯低位帯候補方向で優先度逆転なし)。現時刻 10:10 は 10時台 "
"(日中帯) に移行済み — 9時台 6 セット ~2.2% は朝帯低位帯概ね確定, 日中帯 (10-12時台) は K-Z3 仮説の元来の対象帯 "
"(10:41-11:47 JST 突発パターン再発窓) で K-Z3 traffic 依存説の検証に有意。live smoke 200 (/, /signup; pre-run monitor 計測 200)。"
"host load1 134 (10:09 pre-run uptime 実測, gate 7.5 大幅超過) — rank は測定せず状態正本の更新のみで影響なし。"
"secret は一切記録せず。NEXT: 委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 10時台 n 積み増し続行, "
"次 run ID は run544 使用 — run538..543 消費済みのため次セットは run544)。"
)

HDR = "## Iteration log\n"
if d.count(HDR) != 1:
    sys.exit("HEADER-COUNT-UNEXPECTED %d" % d.count(HDR))

idx = d.index(HDR) + len(HDR)
out = d[:idx] + entry + "\n" + d[idx:]
open(path, 'w', encoding='utf-8').write(out)
print("INSERTED ok len=%d" % len(out))