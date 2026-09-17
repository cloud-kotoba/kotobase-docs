import io
lines = io.open('query-cosientist.md', encoding='utf-8').read().splitlines()
for i in (417, 418, 419, 420):
    print('LINE', i, 'len', len(lines[i - 1]))
    print(lines[i - 1][:200])
    print('...')
# K-Z4 occurrences context
for i, l in enumerate(lines):
    if 'K-Z4' in l:
        print('KZ4 AT LINE', i + 1, 'len', len(l))
