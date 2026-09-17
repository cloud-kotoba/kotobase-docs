import statistics

def pctl_rank(sorted_vals, p):
    n = len(sorted_vals)
    if n == 0:
        return None
    rank = int((p / 100.0) * n + 0.5)
    if rank < 1:
        rank = 1
    if rank > n:
        rank = n
    return sorted_vals[rank - 1]

def load(fn, status='200'):
    times = []
    codes = {}
    for line in open(fn):
        parts = line.split()
        if len(parts) >= 2:
            codes[parts[0]] = codes.get(parts[0], 0) + 1
            if parts[0] == status:
                times.append(float(parts[1]))
    times.sort()
    return times, codes

def report(label, fn):
    t, codes = load(fn)
    cold = [x for x in t if x >= 0.5]
    warm = [x for x in t if x < 0.5]
    p50 = pctl_rank(t, 50)
    warm_p50 = pctl_rank(warm, 50) if warm else None
    mx = t[-1] if t else None
    n = len(t)
    def f(ms):
        return None if ms is None else round(ms, 3)
    print(f"{label}: n={n} codes={codes} cold={len(cold)} cold_list_s={[round(x,4) for x in cold]} "
          f"p50_s={f(p50)} warm_p50_s={f(warm_p50)} max_s={f(mx)}")

report("run281A", "_co_run281A.txt")
report("run281B", "_co_run281B.txt")
report("run281C", "_co_run281C.txt")
report("land281 (control)", "_co_land281.txt")