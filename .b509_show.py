# -*- coding: utf-8 -*-
p = "/tmp/b508_edit.md"
with open(p, "r", encoding="utf-8") as f:
    lines = f.read().split("\n")
for i, ln in enumerate(lines, 1):
    if "run508" in ln:
        print("LINE", i, "|", ln[:220])