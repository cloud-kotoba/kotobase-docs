import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().split("\n")
print("total_lines", len(lines))
# find K-Z3 hypothesis row
for i,l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        print("KZ3_ROW", i)
# find Iteration log
for i,l in enumerate(lines):
    if l.strip().startswith("## Iteration log"):
        print("ITERLOG", i)
# find last evidence entry line preceding iterlog (in K-Z3 cell)
# find run317 reference
for i,l in enumerate(lines):
    if "run317" in l:
        print("RUN317", i, l[:80])
# tail of K-Z3 cell around iterlog