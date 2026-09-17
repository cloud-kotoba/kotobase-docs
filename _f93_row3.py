fn = "query-cosientist.md"
L = open(fn, encoding="utf-8").read().split("\n")
for i, l in enumerate(L):
    if l.startswith("| K-Z2 |") or l.startswith("| K-Q1 |") or l.startswith("| K-S1 |") or l.startswith("| K-S2 |"):
        print(i+1, l.strip()[:60])
print("--- lines 233-251 ---")
for i in range(232, 252):
    print(i+1, "|", L[i][:60])