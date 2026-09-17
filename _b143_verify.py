#!/usr/bin/env python3
path="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s=open(path).read()
lines=s.split("\n")
print("L279 (idx278) TAIL200:",repr(lines[278][-200:]))
print()
for i in range(357,361):
    print("IDX",i,":",repr(lines[i][:110]))
print()
print("run336 mentions:",sum(1 for l in lines if "run336" in l))
print("run337 mentions:",sum(1 for l in lines if "run337" in l))