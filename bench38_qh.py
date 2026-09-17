import os, re
hits = []
for fn in os.listdir("."):
    if not fn.endswith(".md"):
        continue
    try:
        with open(fn, encoding="utf-8", errors="replace") as f:
            for i, line in enumerate(f, 1):
                if re.search(r"quiet-host|要 quiet", line):
                    hits.append(f"{fn}:{i}: {line.strip()[:200]}")
    except IsADirectoryError:
        pass
with open("bench38_qh_out.txt", "w") as f:
    f.write("\n".join(hits) if hits else "NO MATCHES\n")
print("done", len(hits))
