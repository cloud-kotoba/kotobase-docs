import statistics, io

p = "_f112_run246_out.txt"
data = {}
order = []
for line in io.open(p, encoding="utf-8"):
    parts = line.split()
    if not parts or parts[0] not in ("run246A","run246B","run246C","control"):
        continue
    grp = parts[0]
    code = parts[1]
    t = float(parts[2])
    if grp not in data:
        data[grp] = {"codes":[], "times":[]}
        order.append(grp)
    data[grp]["codes"].append(code)
    data[grp]["times"].append(t)

def p50(xs):
    s = sorted(xs)
    n = len(s)
    return s[n//2]

for g in order:
    d = data[g]
    ts = d["times"]
    cold = [t for t in ts if t >= 0.5]
    print(f"{g}: n={len(ts)} all200={all(c=='200' for c in d['codes'])} "
          f"cold>={0.5}s count={len(cold)} {[round(c,4) for c in cold]} "
          f"p50={round(p50(ts),3)}ms max={round(max(ts),3)}ms")

# combined correctness
total = sum(len(data[g]["times"]) for g in order)
all200 = all(c=="200" for g in order for c in data[g]["codes"])
print(f"TOTAL {total} requests, all 200 = {all200}")