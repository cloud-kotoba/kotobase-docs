import io, subprocess

docs = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/'
src = docs + 'query-cosientist.md'

with io.open(src, encoding='utf-8') as f:
    lines = f.read().split('\n')

# Locate the misplaced evidence line (index 236) and its preceding marker line 235 (idx)
mis_idx = None
for n, l in enumerate(lines):
    if l.startswith(' falsify 2026-09-06 (第86回, K-Z3 14時台帯初計測 run212A–C'):
        mis_idx = n
        break
assert mis_idx is not None, 'misplaced line not found'
ev_line = lines.pop(mis_idx)  # remove standalone line
# find where to append: the continuation line right before it (idx mis_idx-1), append with space
prev = lines[mis_idx - 1]
lines[mis_idx - 1] = prev + ' ' + ev_line.strip()

with io.open(src, 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

# verify
with io.open(src, encoding='utf-8') as f:
    ls = f.read().split('\n')
out = []
for n, l in enumerate(ls):
    if 'run212A' in l:
        out.append('line %d len=%d TAIL120: %s' % (n+1, len(l), l[-120:]))
out.append('total lines: %d' % len(ls))
with io.open('/tmp/_f86_fix.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(out) + '\n')
