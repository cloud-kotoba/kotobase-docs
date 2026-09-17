p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().split("\n")
for i in range(2752, 2762):
    print(i + 1, ":", lines[i][:150])
