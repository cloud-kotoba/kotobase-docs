#!/usr/bin/env python3
import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path,"r",encoding="utf-8") as f: txt=f.read()

header = "## Iteration log\n"
i = txt.find(header)
if i < 0:
    raise SystemExit("iter log header not found")
j = i + len(header)

entry = (
"- 2026-09-07: rank 第120回。00:47 JST tick。HEAD 73d431a = remote net-kotobase/main 一致 (fetch net-kotobase + rev-parse 比較, 乖離 0; worktree detached HEAD のため fetch 系で取り込み, origin は未設定・pull --ff-only 不可)。rank 第119回 (19a576a, 00:33) 以降の新規確定 evidence は 1 commit — bench 第110回 run272A-C (73d431a, 00:39, 24時台(0時台) n 積み増し, cold 2/60 ~3.3% — run272A 散発 2/20 1.16/1.43s, B/C 0/20 即消失, control cold 0/20 p50 0.042s 完全静穏で分離成立, run271A 6/20 heavy の振幅内低め位置)。取り込み判定: (a) K-Z3: run272 を取込 24時台通算 = run268 2/60 + run269 3/60 + run270 1/60 + run271 7/60 + 本 tick 2/60 = 15/300 (~5.0%) の 6 セット連続 cold>0 — 深夜帯 24/0時台 (traffic 最低帯) で帯初から 6 セット連続 cold>0 (散発減弱 \u2192 heavy 再上振れ \u2192 散発減弱の振幅, run271A heavy 6/20 は本 tick で非再現) は K-Z3 traffic 依存説への反証材料を継続 (深夜帯 ~26-31% 平坦パターンと整合方向)。ただし全セット「帯内 1 窓即消失」型で帯水準確定・機構判断には未達 (追加 n 継続、fallback 専門のまま)。(b) K-Q1: 変動なし — transact 401 全静的切れ手 (a)/(i)/(ii)/(iii) は棄却済みで残余は cosientist 実装専任の動的切れ手 (biscuit delegation-for-request 動的照合) のみ, KV read 内訳初実測は滞留継続のまま最上位維持。(c) K-Z2/K-S1/K-S2: 変動なし (evidence なし)。status 遷移なし (transition 要件を満たす新 evidence なし: K-Q1 は cosientist 実装待ち, K-Z3 は観測継続・24時台 15/300 ~5.0% は帯水準確定・機構判断に至らず, K-Z2/K-S1/K-S2 は evidence なし)。新仮説なし。evolve 判断なし (合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 24時台 ~5.0% は順位を変えない)。live smoke 200 (/, /signup; pre-run 計測)。host load1 26.13/25.30/26.04 (00:47 uptime 実測, gate 7.5 超過) — rank 担当は測定を行わず状態正本の更新のみで gate 超過は rank 作業に影響なし。secret は一切記録せず。\n  NEXT: K-Z3 24時台(0時台) n 積み増し継続 — 24時台は 6 セット連続 cold>0 で通算 15/300 (~5.0%) の低〜中位帯候補 (run269A 3/20 \u2192 run270A 1/20 散発減弱 \u2192 run271A 6/20 heavy 再上振れ \u2192 run272A 2/20 散発減弱の振幅確認, heavy は帯内 1 窓型で非定着) が立ち、現時刻 0時台(24時台) の間は 24時台 n 積み増し、時間帯移行後は次の帯初/帯確定へ (深夜帯 ~26-31% 平坦パターンへの収束か 24時台限局かは追加 n 継続のみで判別)。host load gate 超過時は production HTTP フォールバックの従来手順, 次 run ID は run273 使用。K-Q1 は cosientist 実装専任のまま rank 測定指示対象外 (正規 tenant write path 経由の biscuit delegation 動的照合)。\n"
)

new_txt = txt[:j] + entry + txt[j:]
with io.open(path,"w",encoding="utf-8") as f:
    f.write(new_txt)
print("OK iter appended, newlen", len(new_txt))