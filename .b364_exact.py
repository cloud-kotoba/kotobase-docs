import io
with io.open("query-cosientist.md", "r", encoding="utf-8") as f:
    c = f.read()
tail = c[-260:]
with io.open("/tmp/exact_tail.txt", "w", encoding="utf-8") as f:
    f.write(tail)
print("ok")