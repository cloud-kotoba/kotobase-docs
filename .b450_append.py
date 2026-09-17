import sys

doc = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
evpath = '/tmp/fz_ev450.txt'

with open(evpath, encoding='utf-8') as f:
    ev = f.read().strip()

with open(doc, encoding='utf-8') as f:
    content = f.read()

lines = content.split('\n')

# locate the K-Z3 hypothesis row (must start with '| K-Z3 | worker |')
idx = None
for i, l in enumerate(lines):
    if l.startswith('| K-Z3 | worker |'):
        idx = i
        break
assert idx is not None, 'K-Z3 row not found'
assert len(ev) > 0, 'empty evidence'

lines[idx] = lines[idx] + ' ' + ev

out = '\n'.join(lines)
with open(doc, 'w', encoding='utf-8') as f:
    f.write(out)

# count occurrences of the run450 marker
cnt = out.count('run450A')
print('run450A occurrences after append:', cnt)
print('K-Z3 row line index:', idx + 1)
print('total_lines:', len(lines))