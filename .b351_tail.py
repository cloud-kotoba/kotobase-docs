import io
for ln in io.open("query-cosientist.md", encoding="utf-8"):
    if ln.startswith("- 2026-09-07: rank 第157回。"):
        print(ln.rstrip("\n")[-80:])
        break
else:
    print("RANK157 NOT FOUND")