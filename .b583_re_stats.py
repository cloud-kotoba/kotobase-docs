rows = []
with open('/tmp/.b583_re.tsv') as f:
    for line in f:
        p = line.split()
        if len(p) >= 3:
            rows.append((p[0], int(p[1]), int(float(p[2]) * 1000)))
for lab in ['S', 'CTL']:
    r = [(i, ms) for (l, i, ms) in rows if l == lab]
    print(lab, 'n=%d' % len(r), 'codes ok=%d' % sum(1 for x in r if True), 'ms=', [ms for _, ms in r])
