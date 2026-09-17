fn = "query-cosientist.md"
L = open(fn, encoding="utf-8").read().split("\n")
for kw in ["run220", "run219", "run218"]:
    hits = [i+1 for i,l in enumerate(L) if kw in l]
    print(kw, "lines:", hits, "->", [(h, L[h-1][:50]) for h in hits][:5])