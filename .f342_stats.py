#!/usr/bin/env python3
# K-Z3 run342 stats: cold(>=0.5s TTFB), nearest-rank p50, warm_p50, max, all200.
import sys, statistics

def load(path):
    codes = []
    times = []
    try:
        with open(path, encoding="utf-8") as f:
            for line in f:
                p = line.split()
                if len(p) >= 2:
                    try:
                        codes.append(int(p[0])); times.append(float(p[1]))
                    except ValueError:
                        pass
    except FileNotFoundError:
        return {"codes": [], "times": []}
    return {"codes": codes, "times": times}

def nearest_rank_p50(vals):
    n = len(vals)
    if n == 0:
        return None
    st = sorted(vals)
    idx = min(int(0.5 * n), n - 1)
    return st[idx]

def summarize(label, d):
    times = d["times"]
    codes = d["codes"]
    valid = times
    cold = sum(1 for t in valid if t >= 0.5)
    p50 = nearest_rank_p50(valid)
    warm = [t for t in valid if t < 0.5]
    warm_p50 = nearest_rank_p50(warm)
    mx = max(valid) if valid else None
    all200 = all(c == 200 for c in codes) if codes else False
    line = (f"{label}: cold={cold}/20 p50={round(p50*1000,1) if p50 is not None else None}ms "
            f"warm_p50={round(warm_p50*1000,1) if warm_p50 is not None else None}ms "
            f"max={round(mx*1000,1) if mx is not None else None}ms all200={all200}")
    print(line)
    return dict(label=label, cold=cold, p50=p50, warm_p50=warm_p50, mx=mx, all200=all200)

def main():
    base = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
    results = {}
    for label, path in [("A", ".f342_342A.txt"), ("B", ".f342_342B.txt"),
                        ("C", ".f342_342C.txt"), ("CTRL", ".f342_land.txt")]:
        results[label] = summarize(label, load(base + "/" + path))
    tcold = results["A"]["cold"] + results["B"]["cold"] + results["C"]["cold"]
    print(f"SEARCH cold={tcold}/60")
    with open(base + "/.f342_stats.txt", "w", encoding="utf-8") as f:
        for label in ["A", "B", "C", "CTRL"]:
            r = results[label]
            f.write(f"{label} cold={r['cold']}/20 p50={r['p50']} warm_p50={r['warm_p50']} max={r['mx']} all200={r['all200']}\n")
        f.write(f"SEARCH cold={tcold}/60\n")
    sys.exit(0 if tcold >= 0 else 1)

if __name__ == "__main__":
    main()