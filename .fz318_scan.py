p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().split("\n")
# scan cell region 279..356 (1-based) for run315/316/317/318 evidence and rank138/139/140 fold notes
for i in range(279, 358):
    l = lines[i-1]
    if any(k in l for k in ["run315","run316","run317","run318","第145回","第146回","第131回","取込"]):
        print(i, "LEN", len(l), "|", l[:60], "|||", l[-60:])