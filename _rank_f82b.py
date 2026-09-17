p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().splitlines()
for i, line in enumerate(lines, 1):
    if "falsify 第82回" in line and "run205A" in line and ("cold" in line):
        print(i, line[:2500])
