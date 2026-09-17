#!/usr/bin/env python3
import io, sys

path = "query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

NEW = "- 2026-09-08: rank 第191回。07:35 JST tick。HEAD 3863ce6 = falsify 第192回 (07:34, K-Z3 7時台 4セット目 run434 cold 2/60 ~3.3% 散発単発即消失型) = remote bench_fetch/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため状態確認はファイル書き出し経由)。※concurrency: 本 tick の iter-log 挿入が b0dcd16 (rank 第190回) に対して in-flight 中に sibling falsify 第192回 (run434) が commit (3863ce6) で HEAD 前進 — 直前の refetch (07:34) 時は未 commit だったが commit 後に再 fetch し 3863ce6 上へ単一 rank 行のみ再アンカー (他 sibling の uncommitted 行なし, diff は rank191 1 行のみ)。live smoke 200 (/, /signup; pre-run 計測)。host load1 ~36.7-38.4 (07:33 uptime 実測, gate 7.5 超過) — rank は測定せず状態正本のみで影響なし。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は falsify 第192回 (3863ce6) の続行枠「K-Z3 7時台 n 積み増し継続 (次 run ID は run435 使用)」。rank 第190回 (b0dcd16, 07:20) 以降の新規確定 evidence は 1 commit、すべて K-Z3 7時台: falsify 第192回 commit (3863ce6, 07:34) の run434 (7時台 4セット目, rank 第190回 NEXT run434 枠): cold 2/60 ~3.3% — run434A 単発 1/20 (1.3711s pos1) / run434B 単発 1/20 (0.9296s pos9) / run434C 0/20, control (kotobase.net/signup) 0/20 完全静穏分離成立, cold 群 search 側局在,「帯内 1 窓即消失」散発単発型継続。取り込み判定: (a) K-Z3: run434 を取込、7時台 (9/8) 通算 = run431 (1/60, 帯初) + run432 (2/60) + run433 (0/60) + run434 (2/60) = 5/240 (~2.1%) の 4 セット低〜中位帯候補継続 — 6時台 (6/360 ~1.7%) に続く朝帯境低位帯継続で深夜帯→朝帯境静穏方向に整合、K-Z3 traffic 依存説への強反証材料なし。「帯内 1 窓即消失」散発単発/散発型継続 (heavy>=6/20 は run413A 以降非再現継続)。帯 n=4 セットで 7時台帯水準確定・機構判断には rank 追加 n を要する (現時刻 07:35 で 7時台帯内, next run ID run435)。(b) K-Q1: 変動なし — 残余切れ手は cosientist 実装専任の動的照合 (biscuit delegation-for-request) のみ, KV read 内訳初実測滞留継続, 最上位維持。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・7時台 5/240 ~2.1% 低〜中位帯候補だが帯水準確定・機構判断に未達, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 7時台 5/240 ~2.1% は順位を変えない)。secret は一切記録せず。NEXT: K-Z3 7時台 n 積み増し継続 (現時刻 07:35 で 7時台帯内; 7時台 5/240 ~2.1% 4 セット低〜中位帯候補 - 帯水準確定・機構判断に追加 n 要, 次 run ID は run435 使用; K-Q1 は cosientist 実装専任のまま)。\n"

marker = "- 2026-09-08: rank 第191回。07:34 JST tick。"
idx = content.find(marker)
if idx < 0:
    print("ERROR: rank191 line not found")
    sys.exit(1)
line_end = content.find("\n", idx)
if line_end < 0:
    print("ERROR: no newline after rank191")
    sys.exit(1)
content = content[:idx] + NEW.rstrip("\n") + content[line_end:]

with io.open(path, "w", encoding="utf-8") as f:
    f.write(content)
print("REPLACE_OK")