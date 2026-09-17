lines = open('query-cosientist.md', encoding='utf-8').read().split('\n')
hits = []
for i,L in enumerate(lines:
    if 'K-Z1/K-Z2 の日中帯短時間スケール再発' in L:
        hits.append(i+1)
print('KZ3_headers', hits
for h in hits:
ef=lines[h-1]
print('row', h, 'len', len(ef), 'tail>>>' + repr(ef[-80:]
# iter-log location
for i,L in enumerate(lines:
    if L.strip() == '## Iteration log':
        print('iterlog_line', i+1, 'next>', lines[i+1][:60]