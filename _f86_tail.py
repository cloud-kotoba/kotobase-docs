import io

docs = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/'
src = docs + 'query-cosientist.md'
with io.open(src, encoding='utf-8') as f:
    lines = f.read().split('\n')
out = []
for n, l in enumerate(lines):
    if l.startswith('| K-Z3 |') or (n > 0 and lines[n-1].startswith('| K-Z3 |')):
        pass
# simpler: print the K-Z3 row tail
for n, l in enumerate(lines):
    if l.startswith('| K-Z3 |'):
        out.append('K-Z3 row line %d len=%d' % (n+1, len(l)))
        out.append('TAIL300: ' + l[-300:])
        # next line
        if n+1 < len(lines):
            out.append('NEXT LINE: ' + lines[n+1][:80])
with io.open('/tmp/_f86_tail.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out) + '\n')
