p = 'query-cosientist.md'
lines = open(p, encoding='utf-8').read().split('\n')
for i, l in enumerate(lines):
    if l.startswith('| K-Z3 |'):
        print('K-Z3 row line no:', i + 1, 'len:', len(l))
        print('TAIL:', repr(l[-260:]))
# also show last 12 lines of file
print('--- file tail ---')
for i, l in enumerate(lines[-14:], start=len(lines) - 13):
    print(i, repr(l[:120]))
