fn = "query-cosientist.md"
L = open(fn, encoding="utf-8").read().split("\n")
for i, l in enumerate(L):
    if l.strip() == "## Iteration log":
        for j in range(i, i + 3):
            print(j + 1, "[" + L[j][:60] + "]")
        break
print("--- ev tail (before header) ---")
for i, l in enumerate(L):
    if l.strip() == "## Iteration log":
        for j in range(i - 2, i):
            print(j + 1, "[" + L[j][:60] + "]")
        break