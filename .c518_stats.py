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
    items = []
    codes = {}
    order = []
    for line in open(fn):
        line = line.strip()
        if not line:
            continue
        parts = line.split()
        if len(parts) < 2:
            continue
        code = parts[0]
        try:
            t = float(parts[1])
        except ValueError:
            continue
        codes[code] = codes.get(code, 0) + 1
        if code == status:
            items.append(t)
            order.append(t)
    items.sort()
    return items, order, codes

def report(label, fn):
    t, order, codes = load(fn)
    cold = [x for x in t if x >= 0.5]
    warm = [x for x in t if x < 0.5]
    p50 = pctl_rank(t, 50)
    warm_p50 = pctl_rank(warm, 50) if warm else None
    mx = t[-1] if t else None
    n = len(t)
    # positions (1-based) of cold events in raw sequence
    cold_pos = [i+1 for i, v in enumerate(order) if v >= 0.5]
    cold_vals = [v for v in order if v >= 0.5]
    pairs = [(cold_pos[i], round(cold_vals[i], 4)) for i in range(len(cold_pos))]
    f = lambda ms: None if ms is None else round(ms, 3)
    print(f"{label}: n={n} codes={codes} cold={len(cold)} cold_pos_s={pairs} "
          f"p50_s={f(p50)} warm_p50_s={f(warm_p50)} max_s={f(mx)}")

report("run518A", ".c518_A.txt")
report("run518B", ".c518_B.txt")
report("run518C", ".c518_C.txt")
report("land518 (control)", ".c518_land.txt")