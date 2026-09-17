# -*- coding: utf-8 -*-
import time
p = "/Users/junkawasaki/github/com/junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = None
for _ in range(15):
    try:
        with open(p, "r", encoding="utf-8") as f:
            txt = f.read()
        break
    except FileNotFoundError:
        time.sleep(0.8)
lines = txt.split("\n")
for i, ln in enumerate(lines, 1):
    if "run508" in ln:
        print(i, "|", ln[:400])