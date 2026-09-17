#!/usr/bin/env python3
import io, sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
new_entry = """- 2026-09-08: rank 第198回。09:51 JST tick。HEAD 9797280 = falsify 第198回 (09:50, K-Z3 9時台 n-add run447 cold 2/60 ~3.3%, control clean separation; HEAD 44271bd = bench 第199回 run446 済) = remote bench_fetch/main・net-kotobase/main 一致 (git fetch + rev-parse 比較 乖離 0; ※本 tick 開始時 working tree に falsify 第198回 run447 の uncommitted iter-log entry があったため ~30s+ refetch で sibling commit (9797280) を待・検証し、その後 ranking 挿入時に再アンカー (diff は rank 第198回 1 行のみ, header=1)。worktree detached HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため状態確認はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 13.58 (09:47 pre-run uptime 実測, gate 7.5 大幅超過) - rank は測定せず状態正本のみで影響なし。※pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 第90回帯 artifact) - true progressive NEXT は iter-log HEAD 連鎖 (rank 第197回→bench 第199回 run446→falsify 第198回 run447)。rank 第197回 (ba2be70, 09:21) 以降の新規確定 evidence は 2 commit、すべて K-Z3: (a) bench 第199回 commit (44271bd) の run446 (9時台 n-add 2セット目): cold 5/60 ~8.3% - run446A 散発 4/20 (0.876/1.028/0.996/1.022s) / B 単発 1/20 (1.416s) / C 0/20, control (kotobase.net/signup) 0/20 完全静穏分離成立。(b) falsify 第198回 commit (9797280) の run447 (9時台 n-add 3セット目, 次枠 run447): cold 2/60 ~3.3% - run447A 散発ペア 2/20 (1.2385s/2.0803s) p50 0.112s / B/C 0/40 即消失, control 0/20 完全静穏 (max 0.259s) 分離成立。取り込み判定: (a) K-Z3: run446 + run447 を取込、9時台 (9/8) 通算 = run445 (2/60, 帯初) + run446 (5/60) + run447 (2/60) = 9/180 (~5.0%) の 3 セット連続 cold>0 - 朝帯境低位帯 (8時台 8/420 ~1.9%) よりやや高位の低〜中位帯候補、深夜帯→朝帯境静穏方向への遷移は 9時台 3 セット連続 cold>0 で弱まる (traffic 依存説への強反証材料なし、帯水準確定には rank 追加 n 要)。「帯内 1 窓即消失」散発単発/ペア型継続 (heavy>=6/20 は run331A 以降非再現継続)。(b) K-Q1: 変動なし - 残余切れ手は cosientist 実装専任の動的照合 (biscuit delegation-for-request) のみ, KV read 内訳初実測滞留継続, 最上位維持。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・9時台 帯水準確定未達, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。secret は一切記録せず。NEXT: K-Z3 9時台 n 積み増し継続 (現時刻 09:51 で 9時台帯内; 9時台 run445+run446+run447 = 9/180 ~5.0% 3 セット済み - 帯水準確定に追加 n 要, 次 run ID は run448 使用; K-Q1 は cosientist 実装専任のまま)。
"""
with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

anchor = "## Iteration log\n- 2026-09-08: falsify 第198回。09:50 JST tick。"
idx = content.find(anchor)
if idx < 0:
    print("ANCHOR NOT FOUND", file=sys.stderr)
    sys.exit(1)

insert_at = idx + len("## Iteration log\n")
new_content = content[:insert_at] + new_entry + content[insert_at:]

with io.open(path, "w", encoding="utf-8") as f:
    f.write(new_content)

hdr_count = new_content.count("## Iteration log")
print("header count:", hdr_count)
print("entry present:", new_entry[:40] in new_content)
print("falsify198 preserved:", "falsify 第198回。09:50 JST tick。" in new_content)
sys.exit(0)