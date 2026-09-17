fn = "query-cosientist.md"
L = open(fn, encoding="utf-8").read().split("\n")
# K-Z3 row is line 222 (index 221). Find where this table row's evidence cell ends:
# look for subsequent lines that start with "|" (new rows) or the NEXT footer
print("=== lines 222-232 (K-Z3 ev continuation) ===")
for i in range(221, 233):
    print(i+1, "|" + L[i][:70])
print("=== search for 'NEXT' and 'K-Z2' row ===")
for i,l in enumerate(L):
    if l.startswith("| K-Z2 |") or ("NEXT:" in l and "委ねる" in l):
        print(i+1, l[:120])