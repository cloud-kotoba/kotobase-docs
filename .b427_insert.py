# insert falsify run427 evidence into K-Z3 row + iter-log entry
fn = 'query-cosientist.md'
def scrub(s):
    return ''.join(ch for ch in s if not (ch <= '\u001f' or '\u200b' <= ch <= '\u200f'))
evo = scrub(open('/tmp/falsify_evo427.txt', encoding='utf-8').read().strip())
ilog = scrub(open('/tmp/falsify_ilog427.txt', encoding='utf-8').read().strip())
text = open(fn, encoding='utf-8').read()
lines = text.split('\n')
kz3_index = None
for i, l in enumerate(lines):
    if l.startswith('| K-Z3 | worker |'):
        kz3_index = i
        break
if kz3_index is None:
    raise SystemExit('K-Z3 row not found')
lines[kz3_index] = lines[kz3_index] + evo
hdr = None
for i, l in enumerate(lines):
    if l.strip() == '## Iteration log':
        hdr = i
        break
if hdr is None:
    raise SystemExit('iter log header not found')
lines.insert(hdr+1, ilog)
open(fn, 'w', encoding='utf-8').write('\n'.join(lines))
print('INSERT-OK kz3', kz3_index+1, 'hdr', hdr+1)