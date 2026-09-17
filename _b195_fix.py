#!/usr/bin/env python3
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_b195_run441.py"
s = open(p, encoding="utf-8").read()
bad = "math.ceil(0.5len(s)))"
good = "math.ceil(0.5 * len(s)))"
if bad in s:
    s = s.replace(bad, good)
    open(p, "w", encoding="utf-8").write(s)
    print("fixed")
else:
    print("bad not found; contains 0.5 lines:")
    for i, ln in enumerate(s.split("\n"), 1):
        if "0.5" in ln:
            print(i, repr(ln))