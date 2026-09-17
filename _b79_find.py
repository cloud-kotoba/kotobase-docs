import io

path = "query-cosientist.md"
with io.open(path, encoding="utf-8") as f:
    lines = f.read().split("\n")
for i, ln in enumerate(lines):
    if "K-Z3" in ln:
        print(i, repr(ln[:120]))
