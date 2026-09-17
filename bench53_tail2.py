p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().splitlines()
# print last 3 iteration entries fully
for i in range(1519, len(lines)):
    print(i+1, lines[i])
