import sys, re

def p50(xs):
    s = sorted(xs)
    n = len(s)
    if n == 0: return 0.0
    return s[(n-1)//2]

groups = {}
order = []
for line in open(sys.argv[1]):
    line = line.strip()
    m = re.match(r'(run263[ABC]|control)\s+(\d+)\s+([0-9.]+)', line)
    if not m: continue
    g = m.group(1)
    code = m.group(2)
    if code != '200':
        print(f"NON200 {g}: {code}")
        continue
    if g not in groups:
        groups[g] = []
        order.append(g)
    groups[g].append(float(m.group(3)))

allx = []
for g in order:
    xs = groups[g]
    allx += xs
    cold = [x for x in xs if x >= 0.5]
    print(f"{g} n={len(xs)} cold={len(cold)}/{len(xs)} allp50={p50(xs)*1000:.1f}ms "
          f"min={min(xs)*1000:.1f}ms max={max(xs)*1000:.1f}ms")
    for idx, x in enumerate(xs):
        if x >= 0.5:
            print(f"   cold @{idx+1} = {x*1000:.1f}ms")

print(f"TOTAL search cold={sum(1 for x in allx if x>=0.5)}/{len(allx)} "
      f"({100*sum(1 for x in allx if x>=0.5)/len(allx) if allx else 0:.1f}%)")