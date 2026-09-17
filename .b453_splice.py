# -*- coding: utf-8 -*-
import io
DOC = 'query-cosientist.md'

with io.open(DOC, encoding='utf-8') as f:
    lines = f.readlines()

# --- append evidence to K-Z3 row (line starting with '| K-Z3 | worker |') ---
kz3_idx = None
for i, l in enumerate(lines):
    if l.startswith('| K-Z3 | worker |'):
        kz3_idx = i
        break
assert kz3_idx is not None, 'K-Z3 row not found'
assert not lines[kz3_idx].rstrip('\n').rstrip().endswith('|'), 'K-Z3 row unexpectedly ends with |'

with io.open('.b453_ev.txt', encoding='utf-8') as f:
    ev = f.read()
ev = ev.strip()
lines[kz3_idx] = lines[kz3_idx].rstrip('\n') + ' ' + ev + '\n'

# --- insert iter-log entry after '## Iteration log' header ---
hdr_idx = None
for i, l in enumerate(lines):
    if l.strip() == '## Iteration log':
        hdr_idx = i
        break
assert hdr_idx is not None, 'iter header not found'

with io.open('.b453_iter.txt', encoding='utf-8') as f:
    iter_txt = f.read()
if not iter_txt.endswith('\n'):
    iter_txt += '\n'

lines.insert(hdr_idx + 1, iter_txt)

with io.open(DOC, 'w', encoding='utf-8') as f:
    f.write(''.join(lines))

# --- verify ---
with io.open(DOC, encoding='utf-8') as f:
    out = f.readlines()
for i, l in enumerate(out):
    if l.strip() == '## Iteration log':
        print('iter header now at line', i + 1)
        print('line after:', out[i + 1][:50])
        break
for i, l in enumerate(out):
    if l.startswith('| K-Z3 | worker |'):
        print('KZ3 row line', i + 1, 'tail90:', repr(l[-90:]))
        break
# count occurrences of the run marker
joined = ''.join(out)
print('b453_ev occurrences:', joined.count('run453A-C'))
print('iter203 occurrences:', joined.count('falsify 第203回'))
print('OK')