import re
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().splitlines()
hits = [(i+1, l) for i, l in enumerate(lines) if "NEXT" in l]
for i, l in hits[-5:]:
    print(i, l[:300])
print("---tail 12---")
for i, l in enumerate(lines[-12:]):
    print(len(lines)-12+i+1, l[:220])
