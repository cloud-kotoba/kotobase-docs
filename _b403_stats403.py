import os

doc = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/"
files = {
    "403A": "_b403_403A.txt",
    "403B": "_b403_403B.txt",
    "403C": "_b403_403C.txt",
    "land": "_b403_land403.txt",
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
for lab, f in files.items():
    rows = read(f)
    if not rows:
        out.append(f"{lab}: NO 200 rows")
        continue
    rows_sorted = sorted(rows)
    n = len(rows_sorted)
    r = max(1, int((0.50 * n) + 0.5))
    p50 = rows_sorted[r - 1]
    cold = sum(1 for x in rows if x >= COLD)
    mx = rows_sorted[-1]
    warm = [x for x in rows if x < COLD]
    wp50 = (sorted(warm)[int((0.50 * len(warm)) + 0.5) - 1] if warm else None)
    wstr = f" warm_p50={wp50*1000:.1f}ms" if wp50 is not None else ""
    out.append(f"{lab}: n={n} p50={p50*1000:.1f}ms cold(>=0.5s)={cold}/{n} max={mx*1000:.1f}ms{wstr}")
allsearch = []
for lab in ("403A", "403B", "403C"):
    allsearch += read(files[lab])
coldtot = sum(1 for x in allsearch if x >= COLD)
out.append(f"SEARCH TOTAL n={len(allsearch)} cold={coldtot}/{len(allsearch)}")
outstr = "\n".join(out)
with open(doc + "_b403_stats403.txt", "w") as fh:
    fh.write(outstr + "\n")
print(outstr)