#!/usr/bin/env python3
import io
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s=io.open(p,encoding="utf-8").read()
lines=s.split("\n")
print("TOTAL LINES", len(lines))
# iteration log HEAD: newest-first, search for 'NEXT' occurrences and recent entries
for i,l in enumerate(lines):
    if "NEXT" in l:
        print("NEXT-LN", i+1, l[:200])
print("=== around iteration log header ===")
for i in range(355, min(380,len(lines))):
    print(i+1, lines[i][:180])