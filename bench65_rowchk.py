import io
doc = io.open("query-cosientist.md", encoding="utf-8").read()
lines = doc.splitlines()
for i in (52, 207):
    l = lines[i - 1]
    print(i, "len", len(l), "last80:", repr(l[-80:]))
