import re
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().splitlines()
for i, line in enumerate(lines, 1):
    if "falsify 第82回" in line and "iteration" not in line.lower() and not line.startswith("|"):
        print("LINE", i)
        print(line[:2200])
