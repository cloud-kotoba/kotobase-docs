#!/usr/bin/env python3
import io, sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

entry = """- 2026-09-08: rank 第186回。06:18 JST tick。HEAD 348875d = falsify 第187回 (06:04, K-Z3 6時台帯初計測 run425 cold 0/60 完全静穏) = remote bench_fetch/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため状態確認はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 30.94 (06:18 uptime 実測, gate 7.5 大幅超過) - rank は測定せず状態正本のみで影響なし。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) - true progressive NEXT は iter-log HEAD (falsify 第187回, 06:04, run425) の続行枠。rank 第185回 (0bf4897, 06:03) 以降の新規確定 evidence は 1 commit、すべて K-Z3: falsify 第187回 commit (348875d) の run425 (6時台帯初計測, rank 第185回 NEXT run425 枠): cold 0/60 完全静穏 - run425A/B/C とも cold 0/20, warm p50 45/40/40ms (p95 126/131/126ms), control (kotobase.net/signup) 0/20 p50 40ms max 122ms 完全静穏分離成立 (search/control とも 0 cold, all 80/80 200)。取り込み判定: (a) K-Z3: run425 を取込、6時台 (9/8) 帯初 = 0/60 完全静穏の 1 セット。6時台は朝帯境の歴朝低位帯 (9/5 run105/115/116/117/118: 2/300 ~0.67% 相当, 9/7 run315-320: 帯通算 7/420 ~1.67%) で帯初 complete-quiet は既存 6時台静穏記録と整合し K-Z3 traffic 依存説の深夜帯→朝帯境静穏方向に弱く整合、強反証材料なし。但し帯初 n=1 セットのみで帯水準確定・機構判断には rank 追加 n を要する。(b) K-Q1: 変動なし - 残余切れ手は cosientist 実装専任の動的照合 (biscuit delegation-for-request) のみ, KV read 内訳初実測滞留継続, 最上位維持。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・6時台 帯水準確定未達, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 - 6時台 0/60 は順位を変えない)。secret は一切記録せず。NEXT: K-Z3 6時台 n 積み増し継続 (現時刻 06:18 で 6時台帯内; run425 6時台帯初 0/60 完全静穏 1 セット済み - 帯水準確定に追加 n 要, 次 run ID は run426 使用; K-Q1 は cosientist 実装専任のまま)。
"""

with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

header = "## Iteration log\n"
idx = content.find(header)
if idx == -1:
    sys.stderr.write("HEADER NOT FOUND\n")
    sys.exit(2)
insert_at = idx + len(header)
new_content = content[:insert_at] + entry + content[insert_at:]
with io.open(path, "w", encoding="utf-8") as f:
    f.write(new_content)
print("inserted, header count now:", new_content.count(header))