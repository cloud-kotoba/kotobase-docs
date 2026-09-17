#!/usr/bin/env python3
import sys, io

PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

entry = """- 2026-09-08: rank 第195回。08:40 JST tick。HEAD c5810a4 = falsify 第196回 (08:34, K-Z3 8時台 run442 cold 0/60 完全静穏) = remote bench_fetch/main 一致 (git fetch bench_fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 系で取込, terminal foreground stdout 空=既知のため状態確認はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 50.39 (08:32 pre-run 実測, gate 7.5 大幅超過) — rank は測定せず状態正本のみで影響なし。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖で、rank 第194回 (08e1e42) の続行枠「K-Z3 8時台 n 積み増し続行 (次 run ID run440)」から falsify195 / bench195 / falsify196 が順次実行済み。rank 第194回 (08e1e42, 08:21) 以降の新規確定 evidence は 3 commit すべて K-Z3 8時台: (a) falsify 第195回 (8b7737f, run440): cold 2/60 (~3.3%) — run440A 単発 1.439s / B 単発 1.122s / C 0/20, control 0/20 完全静穏分離成立。(b) bench 第195回 (ade7b72, run441): cold 1/60 (~1.7%) — run441A 単発 1.4515s, B/C 0/40 + control 0/20 完全静穏分離成立。(c) falsify 第196回 (c5810a4, run442): cold 0/60 完全静穏 — run442A p50 165ms / B 153ms / C 132ms, control 0/20 p50 88ms 静穏分離成立。取り込み判定: (a) K-Z3: run440+441+442 を取込、8時台 (9/8) 通算 = run437 (2/60, 帯初) + run438 (1/60) + run440 (2/60) + run441 (1/60) + run442 (0/60) = 6/300 (~2.0%) 低位帯確定寄り — 「帯内 1 窓即消失」散発単発型継続 (run440A/B・run441A 単発 → run442 完全静穏, heavy>=6/20 は run413A 以降非再現継続)。朝帯境低位帯 (5/6時台 静穏, 7時台 8/360 ~2.2%) の遷移継続で深夜帯→朝帯境静穏方向に整合し K-Z3 traffic 依存説への強反証材料なし、深夜帯 ~26-31% 平坦パターンとの対比も維持。帯別追加 n の限界情報利得は低下済み・本帯は fallback 専門のまま (n=5セット 300試行で 8時台は確定寄り)。(b) K-Q1: 変動なし — 残余切れ手は cosientist 実装専任の動的照合 (biscuit delegation-for-request) のみ, KV read 内訳初実測滞留継続, open 維持・最上位。(c) K-Z2/K-S1/K-S2: 変動なし。status 遷移なし (transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装待ち, K-Z2/K-Z3 は観測継続, K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。secret は一切記録せず。"""

with io.open(PATH, "r", encoding="utf-8") as f:
    content = f.read()

ANCHOR = "## Iteration log\n- 2026-09-08: falsify 第196回"

# anchors: header must appear exactly once; anchor (header+firstentry head) exactly once
hdr_count = content.count("## Iteration log")
anc_count = content.count(ANCHOR)
print("header count:", hdr_count)
print("anchor count:", anc_count)
if hdr_count != 1:
    print("ABORT: header count != 1"); sys.exit(1)
if anc_count != 1:
    print("ABORT: anchor count != 1"); sys.exit(1)

# insert new entry: after the header line, before first entry
new_content = content.replace(
    "## Iteration log\n- 2026-09-08: falsify 第196回",
    "## Iteration log\n" + entry + "\n- 2026-09-08: falsify 第196回",
    1,
)

with io.open(PATH, "w", encoding="utf-8") as f:
    f.write(new_content)

# verify after write
with io.open(PATH, "r", encoding="utf-8") as f:
    check = f.read()
print("verify header count:", check.count("## Iteration log"))
print("verify rank195 present:", "rank 第195回" in check)
# order check: header must precede rank195 which precedes falsify196
i_h = check.index("## Iteration log")
i_r = check.index("rank 第195回")
i_f = check.index("falsify 第196回")
print("order header<rank195<falsify196:", i_h < i_r < i_f)
print("DONE")