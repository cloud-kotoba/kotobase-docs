for f in ['A', 'B']:
    p = '.b531_%s.ttfb' % f
    lines = open(p, encoding='utf-8').read().splitlines()
    last = lines[-20:]
    open(p, 'w', encoding='utf-8').write('\n'.join(last) + '\n')
    print(f, len(lines), '->', len(last))