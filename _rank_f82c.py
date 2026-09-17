p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().splitlines()
# falsify 第82回 standalone iteration log entry
for i, line in enumerate(lines, 1):
    if line.lstrip().startswith("- 2026-09-06: falsify 第82回"):
        print("LOGENTRY", i)
        print(line[:2200])
