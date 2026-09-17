import os, sys
from statistics import median

doc = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/"
files = {
    "294A": "_b294_294A.txt",
    "294B": "_b294_294B.txt",
    "294C": "_b294_294C.txt",
    "land": "_b294_land294.txt",
}
COLD = 0.5  # TTFB >= 0.5s = cold, per claim contract

def read(f):
    rows = []
    with open(doc + f) as fh:
        for line in fh:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) != 2:
                continue
            code, t = parts[0], float(parts[1])
            if code == "200":
                rows.append(t)
    return rows

out = []
smallest_p50 = None
for lab, f in files.items():
    rows = read(f)
    if not rows:
        out.append(f"{lab}: NO 200 rows")
        continue
    rows_sorted = sorted(rows)
    n = len(rows_sorted)
    # nearest-rank p50: ceil(0.50*n), 1-indexed -> rank = (n+1)//2 for odd, n//2+1 for even? nearest-rank: r=ceil(p*n/100)=ceil(0.5n)
    import math
    r = max(1, int(math.floor(0.50 * n + 0.5)))  # nearest-rank ceil logic
    r = max(1, int(math.ceil(0.50 * n)))
    p50 = rows_sorted[r - 1]
    cold = sum(1 for x in rows if x >= COLD)
    mx = rows_sorted[-1]
    out.append(f"{lab}: n={n} p50={p50*1000:.1f}ms cold(>=0.5s)={cold}/{n} max={mx*1000:.1f}ms")
    if smallest_p50 is None or p50 < smallest_p50:
        smallest_p50 = p50
# cold total across search sets
allsearch = []
for lab in ("294A","294B","294C"):
    allsearch += read(files[lab])
coldtot = sum(1 for x in allsearch if x >= COLD)
out.append(f"SEARCH TOTAL n={len(allsearch)} cold={coldtot}/{len(allsearch)}")
outstr = "\n".join(out)
with open(doc + "_b294_stats294.txt", "w") as fh:
    fh.write(outstr + "\n")
print(outstr)