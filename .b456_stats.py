import statistics

def parse_raw(path):
    codes = []
    times = []
    coldpos = []
    i = 0
    with open(path) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            if len(parts) < 2:
                continue
            try:
                code = int(parts[0])
                t = float(parts[1])
            except ValueError:
                continue
            i += 1
            codes.append(code)
            times.append(t)
            if t >= 0.5:
                coldpos.append('%d:%.3fs' % (i, t))
    return codes, times, coldpos

def nearest_rank_p50(vals):
    s = sorted(vals)
    idx = max(1, int(0.50*len(s)) if (0.50*len(s)) == int(0.50*len(s)) and int(0.50*len(s))>=1 else int(0.50*len(s))+1)
    if idx-1 >= len(s):
        idx = len(s)
    return s[idx-1]

def stats_from_raw(path):
    codes, times, coldpos = parse_raw(path)
    if not times:
        return None
    s = sorted(times)
    n = len(s)
    ncold = len(coldpos)
    bad = [c for c in codes if c != 200]
    return {
        'n': n, 'cold': ncold, 'p50': nearest_rank_p50(s),
        'min': s[0], 'max': s[-1],
        'p95': s[max(0, min(n-1, int(0.95*n)-1))],
        'codes': codes, 'coldpos': coldpos, 'badcodes': bad,
    }

with open('/tmp/f456_out.txt', 'w') as fo:
    for label, path in [('run456A', '.b456_run456A_raw.ttfb'),
                        ('run456B', '.b456_run456B_raw.ttfb'),
                        ('run456C', '.b456_run456C_raw.ttfb'),
                        ('landing', '.b456_landing_raw.ttfb')]:
        r = stats_from_raw(path)
        if r is None:
            fo.write('%s: NO DATA\n' % label)
            continue
        line = "%s: n=%d cold(>=0.5s)=%d p50=%.1fms p95=%.1fms min=%.1fms max=%.1fms" % (
            label, r['n'], r['cold'], r['p50']*1000, r['p95']*1000, r['min']*1000, r['max']*1000)
        all200 = (len(r['badcodes']) == 0)
        line += ' all200=%s' % all200
        if not all200:
            line += ' badcodes=%s' % r['badcodes']
        if r['coldpos']:
            line += ' coldpos=' + ','.join(r['coldpos'])
        fo.write(line + '\n')
print('done')