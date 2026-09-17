p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().splitlines()
for i in range(1515, len(lines)):
    print(i+1, lines[i][:260])
