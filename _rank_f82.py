p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = open(p, encoding="utf-8").read()
lines = s.splitlines()
for i, line in enumerate(lines, 1):
    if "第82回" in line or "run205" in line:
        print(i, line[:1200])
