# verify insert
lines = open('query-cosientist.md', encoding='utf-8').read().split('\n')
for i in range(len(lines)):
    l = lines[i]
    if l.startswith('| K-Z3 | worker |'):
        print('KZ3 row', i+1, 'tail', repr(l[-120:]))
        break
print('---')
for i in range(len(lines)):
    l = lines[i]
    if l.startswith('- 2026-09-08: **bench 第189回**'):
        print('BENCH-ILOG line', i+1, 'head', l[:90])
        break