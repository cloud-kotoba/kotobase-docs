# -*- coding: utf-8 -*-
p = "/tmp/b508_committed.md"
with open(p, "r", encoding="utf-8") as f:
    txt = f.read()
lines = txt.split("\n")
print("=== lines 400-407 ===")
for i in range(399, 407):
    print("L%d:" % (i+1), lines[i][:170])
print()
print("=== all run507 occurrences with line numbers ===")
for i, ln in enumerate(lines, 1):
    if "run507" in ln:
        print(i, "|", ln[:200])