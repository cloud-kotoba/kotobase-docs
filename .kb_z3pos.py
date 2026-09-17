import sys
p = "query-cosientist.md"
with open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()
out = []
for i, l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        out.append("line %d len %d" % (i + 1, len(l)))
        out.append("TAIL120: %r" % l[-120:])
sys.stdout.write("\n".join(out) + "\n")