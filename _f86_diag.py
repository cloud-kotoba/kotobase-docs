import io, re

docs = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/'
src = docs + 'query-cosientist.md'

with io.open(src, encoding='utf-8') as f:
    t = f.read()

lines = t.split('\n')
out = []
for n, l in enumerate(lines):
    if 'K-Z3' in l and l.startswith('|'):
        # count occurrences within the row
        out.append('KZ3 row line %d: run211=%d run212=%d len=%d' % (n+1, l.count('run211'), l.count('run212'), len(l)))
    if '第86回' in l:
        out.append('86 line %d: %s... (len %d)' % (n+1, l[:80], len(l)))

with io.open('/tmp/_f86_diag.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out) + '\n')
