path = "query-cosientist.md"
lines = open(path).read().splitlines(keepends=True)
idx = 169
tail = lines[idx][-700:]
print(tail)
