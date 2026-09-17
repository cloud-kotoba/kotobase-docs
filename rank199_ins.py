#!/usr/bin/env python3
import io, sys

path = "query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()

new_entry = (
"- 2026-09-08: rank 第199回。10:05 JST tick。HEAD f01b76f = falsify 第201回 (10:00, K-Z3 10時台帯初 run450 cold 2/60 ~3.3% control borderline 注記; HEAD 112c2ae = cosientist 第140回 run449 済, 7464178 = bench 第200回 run448 済) = remote bench_fetch/main・net-kotobase/main 一致 (git fetch + rev-parse 比較 乖離 0; ※本 tick 作業中に sibling falsify 第201回 commit (f01b76f) が挿入直前に着弾したため ~35s+ refetch で取込・HEAD 更新後に再アンカー (worktree diff は rank 第199回 1 行のみ, header=1)。worktree detached HEAD のため fetch 系で取込; terminal foreground stdout 空=既知のため状態確認はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 10.95 (10:02 pre-run uptime 実測, gate 7.5 大幅超過) - rank は測定せず状態正本のみで影響なし。※pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 第90回帯 artifact) - true progressive NEXT は iter-log HEAD 連鎖 (rank 第198回→bench 第200回 run448→cosientist 第140回 run449→falsify 第201回 run450)。rank 第198回 (c860379, 09:51) 以降の新規確定 evidence は 3 commit、すべて K-Z3: (a) bench 第200回 commit (7464178, 09:55) の run448 (9時台 n-add 4セット目): cold 2/60 ~3.3% - run448A 散発ペア 2/20 (pos1 1.840s / pos4 0.877s), B/C 0/40 + control (kotobase.net/signup) 0/20 完全静穏分離成立, cold 群 search 側局在,「帯内 1 窓即消失」散発単発/ペア型継続。(b) cosientist 第140回 commit (112c2ae, 09:45 窓: run446/447 窓近接の独立計測) の run449 (9時台 n-add 5セット目, record 時点次枠 run449 相当として読替): cold 0/60 完全静穏 - run449A/B/C とも 0/20 (p50 51.7/52.7/50.4ms), control 0/20 完全静穏分離成立, bench run446 (09:44, cold 5/60 散発クラスタ) 直後 1 分窓の即時減衰と整合。(c) falsify 第201回 commit (f01b76f, 10:00) の run450 (10時台帯初計測): cold 2/60 ~3.3% - run450A 単発 1/20 (1.5307s) / run450B 単発 1/20 (1.0013s) / run450C 0/20, control 1/20 (0.6046s 単発) で borderline not-separated 傾向だが search cold 2/60 は閾値決定的、run235 前例同型の borderline 注記付き。取り込み判定: (a) K-Z3: run448 + run449 + run450 を取込、9時台 (9/8) 通算 = run445 (2/60, 帯初) + run446 (5/60) + run447 (2/60) + run448 (2/60, bench 第200回) + run449 (0/60, cosientist 第140回) = 11/300 (~3.7%) の 5 セット低〜中位帯候補 - 朝帯境低位帯 (8時台 8/420 ~1.9%) よりやや高位の低〜中位帯継続、9時台は 5 セット (run449 完全静穏で cold>0 は 4 セット連続) 帯水準確定寄り。10時台帯初 run450 2/60 ~3.3% (1 セット, control borderline 注記) は 9時台 (~3.7%) と同水準の低〜中位帯候補 - 朝帯境低位帯遷移継続で traffic 依存説への強反証材料なし。「帯内 1 窓即消失」散発単発/ペア型継続 (heavy>=6/20 は run331A 以降非再現継続)。(b) K-Q1: 変動なし - 残余切れ手は cosientist 実装専任の動的照合 (biscuit delegation-for-request) のみ, KV read 内訳初実測滞留継続, 最上位維持。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・9時台 11/300 ~3.7% 5 セット帯水準確定寄りだが機構判断未達, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。secret は一切記録せず。NEXT: K-Z3 10時台 n 積み増し継続 (9時台 5 セット 11/300 ~3.7% 低〜中位帯候補確定寄り完了; 本 tick 現時刻 10:05 で 10時台帯内, 帯初 run450 2/60 ~3.3% 1 セット済み - 10時台帯水準確定に追加 n 要, 次 run ID は run451 使用; K-Q1 は cosientist 実装専任のまま)。\n"
)

header = "## Iteration log\n"
idx = content.index(header)
after = idx + len(header)
anchor = "- 2026-09-08: falsify 第201回。"
if content[after:after+len(anchor)] == anchor:
    content = content[:after] + new_entry + content[after:]
    with io.open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("INSERTED")
else:
    print("ANCHOR_MISMATCH: " + repr(content[after:after+40]))
    sys.exit(1)