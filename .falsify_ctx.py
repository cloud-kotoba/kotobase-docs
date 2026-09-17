import re, sys
txt = open('query-cosientist.md', encoding='utf-8').read()
lines = txt.split('\n')
# find K-Z3 hypothesis row
for i, l in enumerate(lines):
    if l.startswith('| K-Z3 |'):
        print('KZ3 line', i+1, 'len', len(l))
        print('TAIL:', l[-800:])
        break
# latest iteration log entries
idx = txt.find('## Iteration log')
print('ITERLOG head:', lines[idx:idx+4])
# last run mention
runs = re.findall(r'run(\d+)', txt)
print('max run:', max(int(r) for r in runs))
