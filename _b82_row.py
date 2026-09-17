with open('query-cosientist.md', encoding='utf-8') as f:
    lines = f.read().splitlines()
# Find the row containing run206 (bench 第81回 evidence) — likely the K-Z3 row in OPEN HYPOTHESES table
for i, l in enumerate(lines):
    if 'run206' in l:
        print('LINE', i, 'len', len(l))
# print the full K-Z3 row (the one at ~35100)
l = [x for x in lines if x.startswith('| K-Z3 ')]
print('K-Z3 rows:', len(l))
if l:
    print(l[0])
