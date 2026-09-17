p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().splitlines()
for i, line in enumerate(lines, 1):
    if ("run205A" in line or "falsify 第81回" in line or "falsify 第82回" in line) and i > 1000:
        print("LINE", i, line[:1600])
        print("---")
