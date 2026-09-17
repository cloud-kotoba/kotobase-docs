s = open('query-cosientist.md').read().split('\n')
for idx in (280, 282):
    row = s[idx]
    print('LINE', idx+1, 'len', len(row))
    print('HEAD:', row[:120])
    print('TAIL:', repr(row[-160:]))
    print('---')
