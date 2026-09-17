import re
d = open('query-cosientist.md', encoding='utf-8').read()
for m in re.finditer(r'run425', d):
    s = max(0, m.start()-100)
    e = min(len(d), m.end()+180)
    print('->', d[s:e].replace('\n', ' ')[:280])
    print()