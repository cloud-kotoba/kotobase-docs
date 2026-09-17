import io, sys
p = 'query-cosientist.md'
lines = io.open(p, encoding='utf-8').read().split('\n')
l = lines[406]
out = io.open('/tmp/t203.txt', 'w', encoding='utf-8')
out.write('len %d\n' % len(l))
out.write(l[-1400:])
out.write('\nDONE\n')
out.close()
print('ok')
