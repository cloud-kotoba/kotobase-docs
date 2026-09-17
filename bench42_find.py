path = "query-cosientist.md"
lines = open(path).read().splitlines()
for i, l in enumerate(lines, 1):
    if l.startswith("| K-Z3"):
        print(i, l[:200])
