#!/usr/bin/env python3
# rank 第151回 iteration-log entry insert (prepend after "## Iteration log")
import io, sys

path = "query-cosientist.md"

entry = """- 2026-09-07: rank 第151回。12:52 JST tick。HEAD d6fb2e1 = bench 第149回 (12:41, K-Z3 12時台 run348 cold 0/60) = remote net-kotobase/main (bench_fetch) 一致 (git fetch + rev-parse 比較, 乖離 0 実測; worktree detached HEAD のため git pull --ff-only 不可, fetch 系で取込; terminal foreground 出力不可の runtime 障害のため状態確認はファイル書き出し経由)。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は falsify 第161回 (Iteration log 先頭, 12:32)「委ねる (rank 指定優先; フォールバックは K-Z3 現在時刻帯 12時台 n 積み増し続行、次 run ID は run348 使用)」の続行枠。rank 第150回 (8e8f56f, 12:26) 以降の新規確定 evidence は 2 件、すべて K-Z3 12時台: (1) falsify 第161回 run347A-C (iter-log 反映, 12:37:02–12:37:19 計測, cold>=0.5s 6/60 — run347A cold 6/20 (1.2721/0.9677/1.9807/1.3052/0.9602/1.2565s 散発クラスタ) p50 99.6ms / B 0/20 60.8ms / C 0/20 85.7ms, control 0/20 p50 84.4ms max 470.1ms 完全静穏で control 分離成立, run347A heavy 6/20 は 12時台 2 回目の heavy 再出現 (run345A 6/20 続き)), (2) bench 第149回 run348A-C (d6fb2e1, 12:39:31–12:39:48, cold 0/60 — A 0/20 p50 78.3ms / B 0/20 68.7ms / C 0/20 98.1ms, control 0/20 p50 185.7ms 静穏, sibling run347A heavy の約 3 分後で全窓静穏)。取り込み判定: (a) K-Z3: run347 + run348 を取込、12時台 (9/7) 通算 = run345 (9/60) + run346 (3/60) + run347 (6/60) + run348 (0/60) = 18/240 (~7.5%) の 4 セット中位帯。run347A cold 6/20 heavy (12時台 2 窓目の heavy: run345A 6/20 → run346 3/60 → run347A 6/20 → run348 0/60) は B/C+control 0/60 + run348 0/60 (約 3 分後) で即減弱し 12時台でも「帯内 1 窓即消失」short-timescale 減弱が維持 — heavy の帯水準持続性は 4 セットでも確認されず単一窓再出現のまま (run331A 9/20 heavy 型は 12時台で帯内 heavy 2 窓再出現するが各即減弱)。12時台 ~7.5% は 11時台 (23/360 ~6.4%) と同水準の中位帯で K-Z3 traffic 依存説の日中帯方向支持を継続 (深夜帯 ~26-31% 平坦パターンとの対比不変)。(b) K-Q1: 変動なし (transact 401 静的切れ手全棄却済み、残余は cosientist 実装専任の動的切れ手、KV read 内訳初実測滞留継続、最上位維持)。(c) K-Z2/K-S1/K-S2: 変動なし。status 遷移なし (transition 要件を満たす新 evidence なし: K-Z3 は観測継続で帯確定段階, K-Q1 は cosientist 実装待ち, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 12時台 18/240 ~7.5% は周辺帯と同水準の継続観測で rank 入れ替えに至る差ではない)。live smoke 200 (/, /signup; pre-run 計測)。host load1 41.66 (12:49 pre-run 実測, gate 7.5 大幅超過) — rank は測定せず状態正本のみ、gate 超過は rank 作業に影響なし。secret は一切記録せず。
- NEXT: K-Z3 current-band(12時台) n-add 継続、次 run ID は run349 使用 (12時台 4 セット 18/240 ~7.5% 中位帯 — 帯内 heavy 2 窓再出現 (run345A/run347A 6/20) の各即減弱を run348 0/60 で確認済み、帯水準確定と heavy 単一窓再出現の持続性の切り分けに追加 n 1 セットが現観測枠, 実行時刻が 12時台内なら継続・13時台移行後は 13時台帯初計測へ)。K-Q1 は cosientist 実装専任のまま rank 測定指示対象外。
"""

anchor = "- 2026-09-07: bench 第149回。12:41 JST tick。HEAD 8e8f56f"

with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

if "rank 第151回" in content:
    print("ABORT: rank 第151回 already present, no insert")
    sys.exit(0)

if anchor not in content:
    print("ABORT: anchor not found:", anchor[:40])
    sys.exit(1)

new_content = content.replace(anchor, entry.rstrip("\n") + "\n" + anchor, 1)
with io.open(path, "w", encoding="utf-8") as f:
    f.write(new_content)

print("INSERTED: added rank 第151回 entry before bench 第149回")