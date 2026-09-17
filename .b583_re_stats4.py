def parse():
    out = []
    with open('/tmp/.b583_re.tsv') as f:
        for line in f:
            p = line.split()
            if len(p) >= 4:
                out.append((p[0], int(p[1]), int(p[2]), round(float(p[3]), 4)))
    return out

rows = parse()
for lab in ['S', 'CTL']:
    r = [x for x in rows if x[0] == lab]
    ms = sorted(x[3] for x in r)
    cold = [x for x in r if x[3] >= 0.5]
    print(lab, 'n=%d' % len(r), '200=%d' % sum(1 for x in r if x[2] == 200),
          'cold=%d' % len(cold), [(x[1], x[3]) for x in cold],
          'p50=%.4f' % ms[len(ms) // 2], 'max=%.4f' % ms[-1], 'min=%.4f' % ms[0])
