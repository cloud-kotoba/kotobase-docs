import sys, io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

entry = "- 2026-09-08: rank 第197回。09:05 JST tick。HEAD 0df64dd = bench 第198回 (09:03, K-Z3 9時台帯初計測 run445 cold 2/60, control clean separation) = remote bench_fetch/main・net-kotobase/main 一致 (git fetch + rev-parse 比較 乖離 0; worktree detached HEAD のため fetch 系で取込, terminal foreground stdout 空=既知のため状態確認はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 52.69 (09:02 pre-run uptime 実測, gate 7.5 大幅超過) — rank は測定せず状態正本のみで影響なし。※pre-run monitor NEXT「委ねる。NEXT: K-Z3 深夜帯 23時台 n 積み増し継続。」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD 連鎖 (rank 第196回→falsify 第197回 run444→bench 第198回 run445)。rank 第196回 (0057d96, 08:52) 以降の新規確定 evidence は 2 commit、すべて K-Z3: (a) falsify 第197回 commit (3c756fc, run444, 8時台 n-add 7セット目): cold 2/60 ~3.3% — run444A 散発 2/20 (1.363s/1.052s), B/C 0/40 + control 0/20 完全静穏分離成立, cold 群 search 側局在, run443 0/60 完全静穏直後の弱い再出現, heavy クラスタは run331A 以降非再現継続。(b) bench 第198回 commit (0df64dd, run445, 9時台帯初計測 09:00): cold 2/60 ~3.3% — run445A 散発 2/20 (1.0246s/1.0157s), B/C 0/40 + control 0/20 完全静穏分離成立, cold 群 search 側局在。取り込み判定: (a) K-Z3: run444 + run445 を取込、8時台 (9/8) 通算 = run437 (2/60, 帯初) + run438 (1/60) + run440 (2/60) + run441 (1/60) + run442 (0/60) + run443 (0/60) + run444 (2/60) = 8/420 (~1.9%) の 7 セット低位帯確定寄り; 9時台 (9/8) 帯初 = run445 2/60 (~3.3%) の 1 セット低〜中位帯候補 — 朝帯境低位帯 (5/6時台 静穏, 7時台 8/360 ~2.2%, 8時台 8/420 ~1.9%) 継続で深夜帯→朝帯境静穏方向に整合、K-Z3 traffic 依存説への強反証材料なし、9時台帯初 2/60 は 8時台 (~1.9%) よりやや高位の低〜中位帯候補で帯水準確定には rank 追加 n 要。「帯内 1 窓即消失」散発単発型継続 (heavy>=6/20 は run331A 以降非再現継続)。(b) K-Q1: 変動なし — 残余切れ手は cosientist 実装専任の動的照合 (biscuit delegation-for-request) のみ, KV read 内訳初実測滞留継続, open 維持・最上位。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・帯水準確定未達, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2)。secret は一切記録せず。NEXT: K-Z3 9時台 n 積み増し継続 (現時刻 09:05 で 9時台帯内; 9時台帯初 run445 2/60 ~3.3% 1 セット済み — 帯水準確定に追加 n 要, 次 run ID は run446 使用; K-Q1 は cosientist 実装専任のまま)。"

# Read file preserving content
with io.open(path, "r", encoding="utf-8") as f:
    text = f.read()

anchor = "## Iteration log\n- 2026-09-08: bench 第198回。09:03 JST tick。"
assert text.count("## Iteration log") == 1, "header count not 1: %d" % text.count("## Iteration log")
assert text.count(anchor) == 1, "anchor not unique: %d" % text.count(anchor)

newtext = "## Iteration log\n" + entry + "\n- 2026-09-08: bench 第198回。09:03 JST tick。"
text = text.replace(anchor, newtext, 1)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(text)

print("inserted OK")
print("header count now:", newtext.count("## Iteration log"))