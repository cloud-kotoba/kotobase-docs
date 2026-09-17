#!/usr/bin/env python3
p = "docs/.b413_stats.py"
with open(p, "r", encoding="utf-8") as f:
    c = f.read()
c = c.replace("/tmp/b412", "/tmp/b413")
with open(p, "w", encoding="utf-8") as f:
    f.write(c)
print("fixed", "/tmp/b413" in c)