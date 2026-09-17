import re
with open('query-cosientist.md', encoding='utf-8') as f:
    text = f.read()
# Find K-Z3 hypothesis row(s) in the OPEN HYPOTHESES table
idx = text.find('K-Z3')
print('first K-Z3 at', idx)
# print table row
for m in re.finditer(r'^\| K-Z3 .*$', text, re.M):
    print('ROW:', m.group(0)[:800])
    print('ROWPOS', m.start())
# Find last 3 iteration log lines
lines = text.splitlines()
print('---tail log lines---')
for i, l in enumerate(lines):
    if '2026-09-06' in l and ('bench 第8' in l or 'bench 第9' in l):
        print(i, l[:300])
print('total lines', len(lines))
