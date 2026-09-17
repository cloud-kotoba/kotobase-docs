#!/usr/bin/env python3
import io,re
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=io.open(p,encoding="utf-8").read().split("\n")
# K-Z3 hypothesis line (line 279 in previous scan). Find all mentions of run3[5-9][0-9]
for i,l in enumerate(lines):
    if "run359" in l or "run360" in l or "run361" in l or "run358" in l:
        print("LN",i+1, l[:400])
        print("---")