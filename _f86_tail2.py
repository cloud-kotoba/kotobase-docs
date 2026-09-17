import io

docs = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/'
src = docs + 'query-cosientist.md'
with io.open(src, encoding='utf-8') as f:
    lines = f.read().split('\n')

# find the line containing our run212 evidence
out = []
for n, l in enumerate(lines):
    if 'run212A' in l:
        out.append('line %d len=%d' % (n+1, len(l)))
        out.append('HEAD120: ' + l[:120])
        out.append('TAIL220: ' + l[-220:])
        if n+1 < len(lines):
            out.append('NEXT LINE 120: ' + lines[n+1][:120])
with io.open('/tmp/_f86_tail2.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out) + '\n')
