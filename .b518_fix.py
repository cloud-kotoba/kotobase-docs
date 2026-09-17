#!/usr/bin/env python3
import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b518_insert.py"
lines = io.open(p, encoding="utf-8").read().split("\n")
for j, ln in enumerate(lines):
    if 'run518 already in iter area' in ln:
        lines[j] = 'assert "falsify 第230回" not in lines[ii+1], "falsify230 dup"'
        print("fixed line", j)
        break
io.open(p, "w", encoding="utf-8").write("\n".join(lines))