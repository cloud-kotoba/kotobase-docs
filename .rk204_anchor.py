import io
p = 'query-cosientist.md'
lines = io.open(p, encoding='utf-8').read().split('\n')
out = io.open('/tmp/anchor.txt', 'w', encoding='utf-8')
for i, l in enumerate(lines):
    if l.strip() == '## Iteration log':
        out.write('HDR at line %d\n' % (i+1))
        out.write('NEXT line %d: %s\n' % (i+2, lines[i+1][:80]))
        out.write('PREV line %d: %s\n' % (i, lines[i-1][:80]))
        break
out.close()
print('ok')
