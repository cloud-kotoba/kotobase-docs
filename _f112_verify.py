import io
p="query-cosientist.md"
lines=io.open(p,encoding="utf-8").readlines()
# K-Z3 row tail
for i,l in enumerate(lines):
    if l.startswith("| K-Z3 |") or l.startswith("| K-Z3|"):
        print("K-Z3 row len:", len(l))
        print("K-Z3 TAIL:", l[-900:])
        break
print("==== iter log top ====")
for i,l in enumerate(lines):
    if l.startswith("## Iteration log"):
        for j in range(i, i+3):
            print(repr(lines[j][:120]))
        break