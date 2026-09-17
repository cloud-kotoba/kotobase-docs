import json, re

data = {}
cur = None
with open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.bench325_out.txt') as f:
    for line in f:
        line = line.strip()
        if line.startswith('==='):
            cur = line.strip('= ').strip('=')
            data[cur] = []
        elif cur and line != 'DONE':
            parts = line.split()
            if len(parts) == 3:
                try:
                    data[cur].append((float(parts[0]), float(parts[1]), int(parts[2])))
                except ValueError:
                    pass

def nearest_rank_p50(vals):
    s = sorted(vals)
    n = len(s)
    idx = max(1, int(__import__('math').ceil(0.5 * n)))
    return s[idx-1]

for w, rows in data.items():
    ttfb = [r[1] for r in rows]
    codes = set(r[2] for r in rows)
    cold = [v for v in ttfb if v >= 0.5]
    print(f"{w}: n={len(ttfb)} all200={codes=={200}} cold>=0.5s={len(cold)}/{len(ttfb)} "
          f"coldvals={[round(v,4) for v in cold]} p50={round(nearest_rank_p50(ttfb),4)}s "
          f"max={round(max(ttfb),4)}s")