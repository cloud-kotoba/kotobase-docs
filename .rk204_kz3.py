import io
p = 'query-cosientist.md'
lines = io.open(p, encoding='utf-8').read().split('\n')
# find K-Z3 row
for i, l in enumerate(lines):
    if l.startswith('| K-Z3 |'):
        out = io.open('/tmp/kz3.txt', 'w', encoding='utf-8')
        out.write('line %d len %d\n' % (i+1, len(l)))
        out.write(l[-2000:])
        out.write('\nHAS run460: %s\n' % ('run460' in l))
        out.write('HAS 11時台 通算 11/240: %s\n' % ('11/240' in l))
        out.close()
        print('found at', i+1)
        break
else:
    print('NOT FOUND')
