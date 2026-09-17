import re
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = open(p, encoding="utf-8").read()
for i, line in enumerate(s.splitlines(), 1):
    if line.startswith("| K-") or "## " in line or "Iteration log" in line.lower():
        print(i, line[:400])
