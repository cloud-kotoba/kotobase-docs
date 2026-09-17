import re
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(path).read().splitlines()
# find K-Z3 row and nearest markers
targets = ["| K-Z1 |", "| K-Z2 |", "| K-Z3 |", "第111回", "run245", "第98回", "run244", "第108回"]
for i, ln in enumerate(lines, 1):
    for t in targets:
        if t in ln:
            print(f"{i}: {ln[:150]}")
            break