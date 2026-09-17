p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().splitlines()
for i, line in enumerate(lines, 1):
    if "run205" in line:
        print("LINE", i, line[:400])
