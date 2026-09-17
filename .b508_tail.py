# -*- coding: utf-8 -*-
p = "/tmp/b508_qc.md"
with open(p, "r", encoding="utf-8") as f:
    txt = f.read()
lines = txt.split("\n")
print("TOTAL_LINES", len(lines))
for i, ln in enumerate(lines, 1):
    if "run508" in ln:
        print("RUN508_MENTION", i, "|", ln[:450])
print("=== K-Z3 evidence row tail (row 279 and continuation) ===")
print("L279:", lines[278][:200])
# print continuation lines after the K-Z3 row header until the next |<ID>|<... row (evidence lines start with spaces)
# Just print rows 279-295
for i in range(278, 296):
    print("L%d:" % (i+1), lines[i][:150])