# -*- coding: utf-8 -*-
p = "/tmp/b508_committed.md"
with open(p, "r", encoding="utf-8") as f:
    txt = f.read()
lines = txt.split("\n")
import re
print("TOTAL_LINES", len(lines))
for i, ln in enumerate(lines, 1):
    if ln.startswith("## Iteration log"):
        print("ITERLOG_HEADER", i)
        for j in range(i, min(len(lines), i+5)):
            s = lines[j].strip()
            if s.startswith("- "):
                print("LOGENTRY", j+1, "|", s[:400])
        break
print("run507", len(re.findall("run507", txt)))
print("run508", len(re.findall("run508", txt)))