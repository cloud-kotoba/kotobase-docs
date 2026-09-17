# -*- coding: utf-8 -*-
import io, sys
P='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
with io.open(P, encoding='utf-8') as f:
    txt=f.read()

ENTRY=("- 2026-09-07: rank 第156回。14:28 JST tick。HEAD 8703e9f = bench 第156回 (14:23, "
"K-Z3 14時台 2 セット目 run360 cold 1/60) (本 commit は local・未 push, remote main = 30e967a = "
"bench 第155回 — bench 第156回 は sweep 済みのため本 rank は run359+run360 を取込)。"
"live smoke 200 (/, /signup; pre-run 計測)。host load1 32.49 (14:17 pre-run uptime 実測, gate 7.5 大幅超過) — "
"rank は測定せず状態正本のみで影響なし。※pre-run monitor NEXT「K-Z3 深夜帯 23時台 n 積み増し継続」は stale "
"(rank 第90回帯 artifact) — true progressive NEXT は bench 第156回 (iter-log, 14:23)「K-Z3 現在時刻帯 14時台 "
"n 積み増し続行、次 run ID は run361 使用」。rank 第155回 (d3a6640, 14:03, fold falsify163-run354 + bench153-run355 "
"+ cosientist124-run356 + bench154-run357 + falsify164-run358 -> 13時台 19/480 ~4.0% 8-set) 以降の新規確定 evidence "
"は 2 commit、すべて K-Z3 14時台: (1) bench 第155回 run359A-C (30e967a, 14:16:14–14:16:30, cold>=0.5s 6/0/1 per 20 "
"= 7/60 ~11.7% — run359A heavy クラスタ 6/20 (0.9694–1.9149s 散発配置), run359B 0/20, run359C 単発 1/20 1.2200s, "
"control 0/20 p50 47.1ms 完全静穏で control 分離成立, cold 群 search 側に局在), (2) bench 第156回 run360A-C "
"(8703e9f, 14:25:55–14:26:10, cold 1/60 ~1.7% — run360A 単発 1.1969s, B/C 0/20 + control 0/20 完全静穏で control "
"分離成立, run359A heavy の 9 分後 1/20 へ減弱)。取り込み判定: (a) K-Z3: run359 + run360 を取込、14時台 (9/7) 通算 "
"= 8/120 (~6.7%) の 2 セット日中高位帯候補。run359A cold 6/20 は heavy (>=6/20) 閾値再達の 14時台帯初初候補 "
"(13時台 run356A 5/20 の帯移行後 1 窓目での heavy 再上振れ, run345A/347A/341A の 12/11時台 heavy 再出現系の後続)、"
"run360 1/60 への 9 分間即減弱で「帯内 1 窓即消失」short-timescale 減弱が 14時台でも 2 セットで維持 "
"(heavy>=6/20 の帯水準持続性は再現未確認, run331A 9/20 heavy 型は単一窓即消失のまま継続)。14時台 8/120 ~6.7% は "
"13時台 (19/480 ~4.0%) より高位・12時台 (25/360 ~6.9%) と同水準の中〜高位帯で日中帯 traffic 依存説の方向支持継続 "
"(深夜帯 ~26-31% 平坦パターンとの対比不変)。帯水準確定は 2 セットで未達 (追加 n 要)。(b) K-Q1: 変動なし "
"(transact 401 静的切れ手全棄却済み、残余は cosientist 実装専任の動的切れ手 biscuit delegation-for-request 動的照合のみ、"
"KV read 内訳初実測滞留継続、最上位維持)。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし "
"(transition 要件を満たす新 evidence なし: K-Z3 は観測継続・帯水準確定未達・機構判断未達, K-Q1 は cosientist 実装待ち, "
"K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし "
"(K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 14時台 8/120 ~6.7% は周辺帯と同水準の継続観測で rank 入れ替えに至る差ではない)。"
"secret は一切記録せず。NEXT: K-Z3 14時台 n 積み増し継続、次 run ID は run361 使用 (14時台 2 セット 8/120 ~6.7% "
"中〜高位帯 — 帯水準確定と heavy 単一窓即消失の持続性・散発減弱確認に帯内追加 n, 実行時刻が 14時台内なら n 積み増し・"
"15時台移行後は 15時台帯初計測へ)。K-Q1 は cosientist 実装専任のまま rank 測定指示対象外。\n")

HDR='## Iteration log\n'
if HDR not in txt:
    sys.exit("HEADER NOT FOUND")
# guard: avoid duplicate insertion
if 'rank 第156回' in txt:
    sys.exit("ALREADY PRESENT")
idx=txt.index(HDR)+len(HDR)
new_txt=txt[:idx]+ENTRY+txt[idx:]
with io.open(P,'w',encoding='utf-8') as f:
    f.write(new_txt)
print("ok inserted")