p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().splitlines()
hits = 0
for i, line in enumerate(lines, 1):
    if "run205" in line and "K-Z3" in line:
        hits += 1
        if hits <= 4:
            print("LINE", i, line[:300])
print("total run205+KZ3 lines:", hits)
