# inspect end chars of K-Z3 row
lines = open('query-cosientist.md', encoding='utf-8').read().split('\n')
for i, l in enumerate(lines):
    if l.startswith('| K-Z3 | worker |'):
        print('LINE', i+1, 'last30', repr(l[-30:]))
        print('ends_with_pipe', l.endswith('|'))
        break