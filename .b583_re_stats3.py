import re
out = []
with open('/tmp/.b583_re.tsv') as f:
    for line in f:
        p = line.split()
        if len(p) >= 3:
            lab, pos = p[0], p[1]
            m = re.search(r'time=\s*([\d.]+)', ' '.join(p[2:]))
            if m:
                out.append((lab, int(pos), round(float(m.group(1)) * 1000)))
for lab in ['S', 'CTL']:
    ms = [v for (l, i, v) in out if l == lab]
    print(lab, 'n=%d' % len(ms), '200s=%d' % len(ms), 'ms=', ms)
