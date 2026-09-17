import statistics

doc = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/"
files = {
    "402A": "_b402_402A.txt",
    "402B": "_b402_402B.txt",
    "402C": "_b402_402C.txt",
    "land": "_b402_land.txt",
}
COLD = 0.5  # TTFB >= 0.5s = cold, per claim contract

def read_rows(f):
    rows = []
    with open(doc + f) as fh:
        for i, line in enumerate(fh, 1):
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) != 2:
                continue
            code, t = parts[0], float(parts[1])
            if code == "200":
                rows.append((i, t))  # (position, ttfb)
    return rows

out = []
for lab, f in files.items():
    pairs = read_rows(f)
    if not pairs:
        out.append(f"{lab}: NO 200 rows")
        continue
    times = [t for (_, t) in pairs]
    times_sorted = sorted(times)
    n = len(times_sorted)
    r = max(1, int((0.50 * n) + 0.5))
    p50 = times_sorted[r - 1]
    colds = [(pos, t) for (pos, t) in pairs if t >= COLD]
    cold = len(colds)
    mx = times_sorted[-1]
    warm = [t for t in times if t < COLD]
    wp50 = (sorted(warm)[int((0.50 * len(warm)) + 0.5) - 1] if warm else None)
    wstr = f" warm_p50={wp50*1000:.1f}ms" if wp50 is not None else ""
    coldstr = ""
    if colds:
        coldstr = " cold_pos=" + ",".join(f"{p}:{t*1000:.0f}ms" for p, t in colds)
    out.append(f"{lab}: n={n} p50={p50*1000:.1f}ms cold(>=0.5s)={cold}/{n} max={mx*1000:.1f}ms{wstr}{coldstr}")
allsearch = []
for lab in ("402A", "402B", "402C"):
    allsearch += [t for (_, t) in read_rows(files[lab])]
coldtot = sum(1 for x in allsearch if x >= COLD)
out.append(f"SEARCH TOTAL n={len(allsearch)} cold={coldtot}/{len(allsearch)}")
outstr = "\n".join(out)
with open(doc + "_b402_stats.txt", "w") as fh:
    fh.write(outstr + "\n")
print(outstr)