p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().split("\n")
H = 357
# rank141 iter-log entry (H+1) - print full
for idx in [H+1, H+2]:
    print("IDX", idx)
    print(lines[idx][:100])
# does K-Z3 evidence cell contain run315/316/317/318 fold notes? check lines 279..357
import re
for i in range(279, 358):
    l = lines[i-1]
    if ("run315" in l or "run316" in l or "run317" in l or "run318" in l) and i != 279:
        # exclude the giant hypothesis row itself
        print("cell ref", i, "LEN", len(l))