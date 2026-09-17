import io, sys

DOC = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
EV = '/tmp/f456_ev.txt'
ILOG = '/tmp/f456_ilog.txt'

with io.open(DOC, 'r', encoding='utf-8') as f:
    content = f.read()
with io.open(EV, 'r', encoding='utf-8') as f:
    ev = f.read().strip()
with io.open(ILOG, 'r', encoding='utf-8') as f:
    ilog = f.read().strip()

# scrub zero-width
content = content.replace('\u200b', '').replace('\u200c', '').replace('\u200d', '')
ev = ev.replace('\u200b', '').replace('\u200c', '').replace('\u200d', '')
ilog = ilog.replace('\u200b', '').replace('\u200c', '').replace('\u200d', '')

# 1. Evidence: append to END of K-Z3 hypothesis row (| K-Z3 | worker | ...)
anchor = '| K-Z3 | worker |'
n_anchor = content.count(anchor)
if n_anchor != 1:
    sys.exit('ANCHOR_COUNT=%d EXPECTED_1' % n_anchor)
start = content.find(anchor)
row_end = content.find('\n', start)
if row_end == -1:
    sys.exit('ROW_END_NOT_FOUND')
row_text = content[start:row_end]
# verify tail looks like the K-Z3 evidence cell end
if not row_text.rstrip().endswith('(rank 専門)。'):
    sys.exit('ROW_TAIL_MISMATCH: ' + row_text.rstrip()[-40:])
new_content = content[:row_end] + ' ' + ev + content[row_end:]

# 2. Iter-log: insert new entry right after header "## Iteration log\n" (newest-first)
hdr = '## Iteration log\n'
hpos = new_content.find(hdr)
if hpos == -1:
    sys.exit('ITER_HEADER_NOT_FOUND')
insert_at = hpos + len(hdr)
# guard: line right after header should start with "- " (existing entries)
nxt = new_content[insert_at:]
new_content = new_content[:insert_at] + ilog + '\n' + new_content[insert_at:]

with io.open(DOC, 'w', encoding='utf-8') as f:
    f.write(new_content)
print('OK')