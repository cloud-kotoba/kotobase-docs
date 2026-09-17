#!/usr/bin/env python3
path="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s=open(path).read()
lines=s.split("\n")
# iterate log header idx=357 (0-based). Print idx 358 (newest entry) and 359
for i in range(358,362):
    if i < len(lines):
        print("=== idx",i,"===")
        print(lines[i])
print("=== ALSO search any line mentioning run336 ===")
for i,l in enumerate(lines):
    if "run336" in l or "run 336" in l:
        print("idx",i,":",l[:100])