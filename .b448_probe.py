import re
md = open('query-cosientist.md', encoding='utf-8').read()
lines = md.split('\n')
for i, l in enumerate(lines):
    if l.startswith('| K-Z3 '):
        print('ROW_LINE', i + 1, 'LEN', len(l))
        print('TAIL:', repr(l[-700:]))
        break
# find committed run IDs near tail to confirm next free
tail = lines[i]
ids = re.findall(r'run(\d{3})', tail[-1200:])
print('RUNIDS in tail window:', ids)