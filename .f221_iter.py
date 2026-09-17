# -*- coding: utf-8 -*-
# falsify 第221回: insert iter-log line at top (after line holding "## Iteration log")
PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
LINE = ("- 2026-09-08: falsify 第221回。19:36 JST tick。HEAD 0735ab0 = bench 第216回 "
"(19:22, K-Z3 19時台 run495 cold 0/60 完全静穏; NEXT 委ねる → 継続) = remote net-kotobase/main 一致 "
"(fetch + rev-parse 乖離 0; detached HEAD のため fetch で取込)。K-Z3 19時台帯 N 積み増し独立 実測 run496A-C "
"+ landing control (n=20 x 3 + 20, 別接続 curl, cold>=0.5s, 19:34:30-19:34:52 JST, host load1 52-103 "
"production HTTP のため gate 外): cold 4/1/0 = 5/60 (~8.3%) - run496A 散発クラスタ 4/20 "
"(0.9671/1.2516/1.3302/1.9902s) p50 129.4ms / B 単発 1/20 p50 158.2ms / C 0/20 p50 93.3ms, "
"landing control cold 0/20 p50 75.5ms 完全静穏で control 分離成立、cold 群は search 側に局在 "
"(run495 完全静穏 0.7=20 分後の爽発で日中帯短時間スケール変動と整合)。19時台通算 5/120 (~4.2%) "
"2 セット。evidence は K-Z3 仮説行 (L279) 末尾に追記済み, iter-log 最上部に 1 行挿入。")

with open(PATH, encoding="utf-8") as f:
    lines = f.readlines()
idx = None
for i, ln in enumerate(lines):
    if ln.startswith("## Iteration log"):
        idx = i
        break
assert idx is not None, "iter-log header not found"
# insert at idx+1 (top of list)
lines.insert(idx + 1, LINE + "\n")
with open(PATH, "w", encoding="utf-8") as f:
    f.writelines(lines)
L2 = open(PATH, encoding="utf-8").read().split("\n")
print("ITER_OCC", sum(1 for l in L2 if "falsify 第221回" in l))
print("SCRUB", "#####" in "\n".join(L2))