sets = {}
cur = None
ctrl = []
src = '.b532k_run649_results.txt'
lines = open(src).read().strip().split('\n')
dbg = ["nlines=%d" % len(lines)]
for line in lines:
    s = line.strip()
    if not s:
        dbg.append("BLANK")
        continue
    if s.startswith('---SET') and s.endswith('END---'):
        name = s.split()[1]
        sets.setdefault(name, [])
        dbg.append("MARKER set %s (size after marker)" % name)
        continue
    if s.startswith('---CONTROL END---'):
        cur = 'CTRL'
        dbg.append("MARKER ctrl")
        continue
    if s.startswith('END '):
        continue
    parts = s.split()
    code, t = parts[0], float(parts[1])
    if cur == 'CTRL':
        ctrl.append((code, t))
    elif cur:
        sets[cur].append((code, t))
    else:
        sets.setdefault('A', []).append((code, t))
dbg.append("sets A/B/C sizes: %d %d %d ctrl=%d" % (len(sets.get('A', [])), len(sets.get('B', [])), len(sets.get('C', [])), len(ctrl)))
open('/tmp/b532k_dbg.txt', 'w').write("\n".join(dbg) + "\n")
