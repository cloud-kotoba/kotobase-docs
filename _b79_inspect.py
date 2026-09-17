import io
with io.open("query-cosientist.md", encoding="utf-8") as f:
    lines = f.read().split("\n")
ln = lines[206]
print("start:", repr(ln[:30]))
print("end:", repr(ln[-120:]))
print("len:", len(ln))
for i in range(204, 238):
    l = lines[i]
    print(i, repr(l[:40]), "...", repr(l[-40:]) if len(l) > 80 else "")
