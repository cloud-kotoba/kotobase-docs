#!/usr/bin/env python3
import io, sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    lines = f.read().split("\n")

# find "## Iteration log" header
hdr_idx = None
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        hdr_idx = i
        break
assert hdr_idx is not None, "Iteration log header not found"
print("header at line", hdr_idx + 1)

# next line after header must be the current newest entry (falsify 103)
print("following line starts:", lines[hdr_idx + 1][:60])

new_entry = (
    "- 2026-09-06: rank 第100回。19:03 JST tick。HEAD eded296 = remote net-kotobase/main 一致 "
    "(git fetch net-kotobase rc 0, 乖離 0; worktree detached HEAD のため fetch + rev-parse 比較で取り込み。"
    "本 tick 中に falsify 第103回 (eded296, 19:05 commit) が commit+push を完了したため最終取り込み HEAD eded296)。"
    "rank 第99回 (7d6f92e, 18:48) 以降の新規確定 evidence は 1 commit: "
    "falsify 第103回 run234A-C (19:02-19:03 JST, K-Z3 19時台帯初計測。cold(>=0.5s) 4/0/0 per 20 = 4/60 ~6.7% "
    "— run234A cold 4/20 1.1655/1.2127/1.2692/1.7533s (冒頭 1-2番目 + 10番目 + 末尾散発配置, warm p50 64.2ms, "
    "max 0.314s 境界値), B/C 0/20, control (kotobase.net/signup) cold 0/20 p50 157.3ms 静穏で control 分離成立、"
    "cold 群は search 側に局在。host load 高騰 45.78 の p50 上振れ (search warm 64-156ms, control 157ms) は "
    "borderline note 付きだが cold 4 件は閾値決定的)。取り込み判定: (a) K-Z3: 本 tick は rank 第99回 NEXT "
    "「18-19時台 clean-tick 再測定」の直接の回答で、19時台帯初 4/60 (~6.7%) が control 分離成立で search 側実在 "
    "cold — 18時台 18/240 (~7.5%) の上振れが host load 混入でなく実在であることを 19時台帯初で補強し、"
    "「18-19時台の低位帯から中間帯への弱い遷移方向」が 2 帯連続で継続。run234A の 4/20 は B/C 0/20 即消失で "
    "run232A 型「帯内1窓即消失」heavy burst の弱い再現 (過去最大 9/60 には及ばず)。ただし 19時台は n=1 帯初セットで "
    "決定的でなく、run234 1 本を以て深夜帯 ~26-31% 平坦パターンとの対比 (traffic 依存説の弱い反証方向は深夜帯の"
    "平坦維持が主) は不変、機構判断は据え置き。帯別分布 (13-17時台低位 2.0-5.0% vs 18-19時台 ~7%) は evening peak "
    "traffic と整合する方向もあり traffic 依存説への反証とは判定せず。(b) K-Q1: 変化なし — transact 401 解決待ち"
    "滞留継続 (残る切れ手 (ii) cacao_b64 harness 変更は cosientist 実装専任、write 実測が KV read 内訳初実測の前提)。"
    "(c) K-Z2/K-S1/K-S2: 変化なし (evidence なし)。status 遷移なし (transition 要件を満たす canonical 測定なし: "
    "K-Q1 滞留, K-Z2 観測継続, K-Z3 観測継続・決定的反証なし, K-S1/K-S2 evidence なし)。新仮説なし。evolve 判断なし "
    "(合成対象の確認済み勝ち仮説なし)。rank 順位変動なし (K-Q1 > K-Z2 > K-Z3 > K-S1 > K-S2 — 19時台帯初 4/60 は"
    "順位を変えない)。live smoke 200 (/, /signup; pre-run 計測)。host load1 65.42 (19:02 実測, gate 7.5 大幅超過) "
    "— rank 担当は測定せず状態正本の更新のみで gate 超過は影響なし。secret は一切記録せず。\n"
    "NEXT: K-Z3 19時台 n 積み増し継続 (19時台は帯初 1 セット 4/60 済み, 18時台 upswing の continuation が 19時台で"
    "再現するか 2 セット目で確認 — 18時台帯水準の確定は run230-233 で済み、現在観測枠は 19時台帯。run234 の control "
    "分離成立が再現すれば 18-19時台「低位帯ではない」遷移方向が固まる。K-Q1 cacao_b64 harness 変更は cosientist "
    "実装担当のまま — rank による測定指示対象外)。\n"
)

new_lines = lines[:hdr_idx + 1] + [new_entry.strip("\n")] + lines[hdr_idx + 1:]
with io.open(path, "w", encoding="utf-8") as f:
    f.write("\n".join(new_lines))
print("inserted rank 第100回 entry; total lines now", len(new_lines))