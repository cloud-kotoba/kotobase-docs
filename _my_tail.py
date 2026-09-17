import io
p = "query-cosientist.md"
line = None
with io.open(p, encoding="utf-8") as f:
    for i, l in enumerate(f, 1):
        if l.startswith("| K-Z3 |") or l.startswith("| K-Z3|"):
            line = l
            print("KZ3 LINE NUM:", i)
            break
if line is None:
    print("K-Z3 not found")
else:
    print("LINE LEN:", len(line))
    # print tail of evidence (last cell)
    print("===TAIL 3500===")
    print(line[-3500:])