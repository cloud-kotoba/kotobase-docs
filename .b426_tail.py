# inspect K-Z3 row tail
lines = open('query-cosientist.md', encoding='utf-8').read().split('\n')
for i, l in enumerate(lines):
    if l.startswith('| K-Z3 | worker |'):
        print('LINE', i+1, 'len', len(l))
        print(repr(l[-200:]))
        break