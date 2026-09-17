lines = open('query-cosientist.md', encoding='utf-8').read().split('\n')
for i,L in enumerate(lines):
    if '日中帯短時間スケール再発' in L:
        print('KZ3_row', i+1, 'len', len(L))
        print('TAIL>>>' + repr(L[-60:])
for i,L in enumerate(lines:
    if L.strip() == '## Iteration log':
        print('ITERLOG_line', i+1, 'next>', lines[i+1][:50]