# -*- coding: utf-8 -*-
import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = io.open(p, encoding="utf-8").read().split("\n")
for i, ln in enumerate(lines, 1):
    if "K-Z3" in ln or "### K-Z3" in ln or ln.startswith("## Iteration log"):
        print(i, "|", ln[:180])
print("--- total lines:", len(lines))