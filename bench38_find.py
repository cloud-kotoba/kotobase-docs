import os, re
hits = []
for fn in sorted(os.listdir(".")):
    if not re.match(r"bench\d+.*\.(py|json|txt)$", fn):
        continue
    try:
        with open(fn, encoding="utf-8", errors="replace") as f:
            content = f.read()
        if "search.kotobase.net" in content or "/search?q=" in content:
            hits.append(fn)
    except IsADirectoryError:
        pass
with open("bench38_find_out.txt", "w") as f:
    f.write("\n".join(hits) if hits else "NONE\n")
print("done", len(hits))
