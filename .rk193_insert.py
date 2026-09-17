#!/usr/bin/env python3
# rank 第193回 iter-log single-line insert (consume '## Iteration log' header, re-emit once)
# Corrected: fold BOTH bench193-run437 + falsify194-run438 on new HEAD 148a308b
import io, sys

PATH = "query-cosientist.md"
HEADER = "## Iteration log"

NEW_ENTRY = "- 2026-09-08: rank 第193回。08:12 JST tick。HEAD 148a308b = falsify 第194回 (08:08(commit), K-Z3 8時台帯内 2セット目 run438 cold 1/60 ~1.7%, control clean separation; HEAD 79f72cf bench 第193回 run437 済) = remote bench_fetch/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため状態確認はファイル書き出し経由)。※concurrency: 本 tick の中で sibling の commit が 2 段前進 — (1) 開始時 working tree に bench 第193回 run437 の uncommitted entry (HEAD 5c0c649 上) があり ~45s 待機 → bench193 commit (79f72cf) を refetch で確認し挿入準備 → (2) 挿入直前にまた falsify 第194回 (run438, 8時台 2セット目) が commit (148a308b) で HEAD 前進したため、一度 discard (git checkout --) して rank193 単一行を 148a308b 上へ再アンカー・再挿入 (commit 直前 worktree diff = rank 1 行のみ, header=1, 他 sibling uncommitted なし, next run ID は falsify 第194回自身の NEXT run439 を継承)。live smoke 200 (/, /signup; pre-run 計測)。host load1 36.56 (08:01 uptime 実測, gate 7.5 超過) — rank は測定せず状態正本のみで影響なし。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は falsify 第194回 (148a308b) の続行枠「K-Z3 8時台 n 積み増し続行 (次 run ID run439)」。rank 第192回 (5c0c649, 07:49) 以降の新規確定 evidence は 2 commit、すべて K-Z3 8時台: (a) bench 第193回 commit (79f72cf, 08:01) の run437 (8時台帯初計測): cold 2/60 ~3.3% — run437A 単発 1/20 (1.419s pos3) / run437B 単発 1/20 (0.964s pos16) / run437C 0/20, control 0/20 完全静穏分離成立。(b) falsify 第194回 commit (148a308b, 08:08) の run438 (8時台帯内 2セット目, bench193 NEXT 委ねるフォールバックの実行枠): cold 1/60 ~1.7% — run438A 単発散発 1/20 (max 887.2ms, p50 52.7ms), B/C 0/40 + control 0/20 完全静穏分離成立 (cold 群 search 側局在,「帯内 1 窓即消失」散発単発型継続, heavy>=6/20 は run413A 以降非再現継続)。取り込み判定: (a) K-Z3: run437 + run438 を取込、8時台 (9/8) 通算 = bench-run437 (2/60, 帯初) + falsify-run438 (1/60) = 3/120 (~2.5%) — 5/6時台 完全静穏 と 7時台 8/360 ~2.2% に続く朝帯境低位帯の遷移継続で深夜帯→朝帯境静穏方向に整合、K-Z3 traffic 依存説への強反証材料なし。帯 n=2 セットのみで 8時台帯水準確定・機構判断には rank 追加 n を要する (現時刻 08:12 で 8時台帯内, next run ID run439)。(b) K-Q1: 変動なし — 残余切れ手は cosientist 実装専任の動的照合 (biscuit delegation-for-request) のみ, KV read 内訳初実測滞留継続, 最上位維持。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・8時台 3/120 ~2.5% だが帯水準確定・機構判断に未達, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 8時台 3/120 ~2.5% は順位を変えない)。secret は一切記録せず。NEXT: K-Z3 8時台 n 積み増し継続 (現時刻 08:12 で 8時台帯内; 8時台 run437+run438 済みで帯 n=2 / 通算 3/120 ~2.5%・帯水準確定に追加 n 要 — 次 run ID は run439 使用)。"

with io.open(PATH, "r", encoding="utf-8") as f:
    txt = f.read()

nhdr = txt.count(HEADER + "\n")
if nhdr != 1:
    print("HEADER_COUNT_NE=%d" % nhdr, file=sys.stderr)
    sys.exit(3)

idx = txt.find(HEADER + "\n")
head_end = idx + len(HEADER + "\n")
rest = txt[head_end:]
insert = NEW_ENTRY + "\n"
new_txt = txt[:head_end] + insert + rest

with io.open(PATH, "w", encoding="utf-8") as f:
    f.write(new_txt)

print("INSERTED_OK header=%d" % new_txt.count(HEADER + "\n"))