fn = "query-cosientist.md"
L = open(fn, encoding="utf-8").read().split("\n")
print("LOGTOP250", L[249][:60])
print("LOGTOP251", L[250][:60])
print("LOGTOP252", L[251][:60])
print("--- K-Z3 row 222 ---")
print(L[221][:500])