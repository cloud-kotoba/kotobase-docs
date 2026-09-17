#!/usr/bin/env python3
import io
FN = "query-cosientist.md"
OLD = "sibling falsify 第152回 (08:03) が run328 (8時台帯初 cold 1/60) を未 commit 在飛実施済み、本 tick は次 run ID run329 で 8時台 n 積み増しとして実施 (在飛 falsify152 の diff は本 commit に同梱 — coherent superset)。"
NEW = "sibling falsify 第152回 (08:03) が run328 (8時台帯初 cold 1/60) を実施し rank 第144回 (85e69b5) が fold 済み、本 tick はその NEXT run329 枠で 8時台 n 積み増しとして実施。"
with io.open(FN, "r", encoding="utf-8") as f:
    s = f.read()
assert OLD in s, "anchor not found"
s = s.replace(OLD, NEW, 1)
with io.open(FN, "w", encoding="utf-8") as f:
    f.write(s)
print("fixed")