import sys, statistics
def nearest_rank_pct(data, p):
    if not data: return None
    s = sorted(data)
    r = (p/100.0)*len(s)
    # nearest-rank: ceil
    import math
    idx = max(1, int(math.ceil(r))) - 1
    return s[idx]
def analyze(fn):
    vals=[]; codes={}
    with open(fn, encoding='utf-8') as f:
        for line in f:
            line=line.strip()
            if not line: continue
            parts=line.split()
            if len(parts)<2: continue
            try:
                code=int(parts[0]); ttfb=float(parts[1])
            except ValueError:
                continue
            codes[code]=codes.get(code,0)+1
            vals.append(ttfb)
    cold=[v for v in vals if v>=0.5]
    return {
        'file':fn,'n':len(vals),'codes':codes,
        'cold':len(cold),'cold_vals':cold,
        'p50':nearest_rank_pct(vals,50),
        'p95':nearest_rank_pct(vals,95),
        'min':min(vals) if vals else None,
        'max':max(vals) if vals else None,
        'mean':statistics.mean(vals) if vals else None,
    }
for fn in sys.argv[1:]:
    r=analyze(fn)
    print("== %s ==" % r['file'])
    print("n=%d codes=%s cold=%d p50=%.4fs p95=%.4fs min=%.4fs max=%.4fs mean=%.4fs" % (
        r['n'], r['codes'], r['cold'], r['p50'], r['p95'], r['min'], r['max'], r['mean']))
    if r['cold_vals']:
        print("  cold: %s" % ", ".join("%.4fs"%v for v in sorted(r['cold_vals'])))