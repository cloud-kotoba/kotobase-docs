#!/usr/bin/env python3
import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    lines = f.read().split("\n")

# find "4. K-S1" line
target = None
for i, ln in enumerate(lines):
    if ln.strip().startswith("4. K-S1"):
        target = i
        break
assert target is not None, "item4 not found"
print("item4 at line", target + 1)

note = (
    "第99-100回の 19時台帯初計測: falsify 第103回 run234A-C (19:02-19:03 JST, cold(>=0.5s) 4/0/0 per 20 = "
    "4/60 ~6.7% — run234A cold 4/20 (1.1655/1.2127/1.2692/1.7533s, 冒頭 1-2番目 + 10番目 + 末尾散発), "
    "B/C 0/20, control cold 0/20 p50 157.3ms 静穏で control 分離成立、search 側実在 cold。host load 45.78 の "
    "p50 上振れ borderline note 付きだが cold 4 件は閾値決定的)。rank 第99回 NEXT の 18-19時台 clean-tick 再測定の"
    "回答: 19時台帯初 4/60 が control 分離成立で 18時台 18/240 (~7.5%) の上振れが実在であることを補強し、"
    "「18-19時台の低位帯から中間帯への弱い遷移方向」が 2 帯連続で継続 (run234A は run232A 型 heavy burst の弱い再現、"
    "過去最大 9/60 には及ばず)。ただし n=1 帯初セットで決定的でなく、深夜帯 ~26-31% 平坦パターンとの対比"
    "(traffic 依存説の弱い反証の主根拠) は不変、機構判断は据え置き。\n"
)

new_lines = lines[:target] + [note.rstrip("\n")] + lines[target:]
with io.open(path, "w", encoding="utf-8") as f:
    f.write("\n".join(new_lines))
print("inserted 19時台 note; total lines", len(new_lines))