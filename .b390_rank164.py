#!/usr/bin/env python3
import io, sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    data = f.read()

lines = data.split("\n")

# locate header
hdr_idx = None
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        hdr_idx = i
        break
# avoid matching a table-cell '## Iteration log' that might appear; assert first match
if hdr_idx is None:
    sys.exit("ERR no header")

# count headers
hc = sum(1 for ln in lines if ln.strip() == "## Iteration log")
if hc != 1:
    sys.exit("ERR header count !=1: %d" % hc)

with io.open("/tmp/b390_status.txt", "w", encoding="utf-8") as g:
    g.write("hdr_idx=%d header_count=%d\n" % (hdr_idx, hc))
    g.write("first_entry_before=[%s]\n" % lines[hdr_idx+1][:60].replace("\n",""))

entry = ( "- 2026-09-07: **rank 第164回**. ~19:05 JST tick\\tHEAD 83bac7a = bench 第170回 (18:48, K-Z3 18時台 n-add run385 cold 2/60) = remote bench_fetch/main 【一致】(git fetch + rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 系で取込; terminal foreground 出力不可=既知のため状態確認はファイル書き出し経由)。live smoke 200 (/, /signup; pre-run 計測)。host load1 39.57 (19:02 uptime 実測, gate 7.5 大幅超過) — rank は測定せず状態正本のみで影響なし。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale (rank 第90回帯 artifact) — true progressive NEXT は iter-log HEAD(bench 第170回, 18:48)「委ねる; フォールバックは K-Z3 現在時刻帯 18時台 n 積み増し続行, 次 run ID は run386 使用」。rank 第163回 (10d256c, ~18:40) 以降の新規確定 evidence は 2 分岐、すべて K-Z3 18時台: (1) falsify 第173回 run384A–C (18:44, in-flight 反映, cold  ̃7/60 ~11.7% — run384 散発配置 7/20, B/C 0/20, control 0/20 完全静穏分離成立, run383 散発型の 16 分後弱い再現,「帯内 1 窓即消失」型継続), (2) bench 第170回 run385A–C (83bac7a, 18:48, cold 1/1/0 per  ̃20 = 2/60 ~3.3% — run385A/B 各単発散発 1.287/1.315s, C 0/20, control 0/20 完全静穏で分離成立, run384 の 4 分後弱い再現,「帯内 1 窓即消失」単発型継続, heavy>=6/20 は再達せず)。取り込み判定: (a) K-Z3: run384 + run385 を取込,in 18時台 (9/7) 通算 = run381(2/60) + run382(4/60) + run383(7/60) + run384(7/60) + run385(2/60) = 22/300 (~7.3%) の 5 セット中位帯候補 — 帯内 heavy 2 窓 (run368A/373A/377A heavy 型の再出現以降, 5 セットとも「帯内 1 窓即消失」short-timescale 減弱が維持 (heavy 帯水準持続性は単一窓非持続のまま再現未確認; 18時台 ~7.3% は 17時台 (27/360 ~7.5%) と同水準の日中帯高位帯横断継続, traffic 依存説の日中帯方向支持継続, 深夜帯 ~26-31% 平坦パターンとの対比不変)。(b) K-Q1: 変動なし (transact 401 静的切れ手全棄却済み, 残余は cosientist 実装専任の動的切れ手 biscuit delegation-for-request 動的照合のみ, KV read 内訳初実測滞留継続, 最上位維持)。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・帯水準確定未達, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 18時台 22/300 ~7.3% は順位を変えない)。secret は一切記録せず (curl のみ)。NEXT: K-Z3 19時台帯初計測 run386 使用 (18時台 5 セット 22/300 ~7.3% 中位帯候補完了 — 現時刻帯 19時台へ移行; falsify/bench が 19時台帯初 n=1 セット実施, host load gate 超過時は production HTTP フォールバックの従来手順 — K-Q1 は cosientist 実装専任のまま (rank 測定指示対象外)。" )

new_lines = lines[:hdr_idx+1] + [entry] + lines[hdr_idx+1:]
out = "\n".join(new_lines)

# verify header count still 1
nc = sum(1 for ln in new_lines if ln.strip() == "## Iteration log")
if nc != 1:
    sys.exit("ERR after-insert header count !=1: %d" % nc)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(out)
