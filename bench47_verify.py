with open("query-cosientist.md", encoding="utf-8") as f:
    txt = f.read()
i = next(i for i, ln in enumerate(txt.split("\n")) if ln.startswith("| K-Z3 "))
tail = txt.split("\n")[i][-500:]
with open("bench47_verify.txt", "w", encoding="utf-8") as out:
    out.write(tail)
print("ok", len(txt))
