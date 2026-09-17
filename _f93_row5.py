fn = "query-cosientist.md"
L = open(fn, encoding="utf-8").read().split("\n")
for i,l in enumerate(L):
    if "| K-Z2 |" in l:
        print(i+1, l.strip()[:50])
print("--- lines 248-252 raw ---")
for i in range(247, 252):
    print(i+1, "[" + L[i] + "]")