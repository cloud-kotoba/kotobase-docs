p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().split("\n")
keys = ["run314","run315","run316","run317","run319","第144回","第145回","第146回","第132回","第138回"]
for i,l in enumerate(lines):
    for k in keys:
        if k in l:
            print(i, k, "|", l[:70])
            break
# print the raw last 6 lines of the K-Z3 cell block (0-based 351-356) full length
print("== full tails ==")
for i in range(351, len(lines)):
    if i>=358: break
    print("LINE", i, "LEN", len(lines[i]))
    print(lines[i][:150])
    print(lines[i][-150:])