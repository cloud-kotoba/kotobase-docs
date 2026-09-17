import re
txt = open('query-cosientist.md', encoding='utf-8').read()
for m in re.finditer(r'## Iteration log', txt):
    print(m.start(), repr(txt[m.start()-20:m.start()+40]))
print('run IDs run58x:', sorted(set(re.findall(r'run58[0-9]', txt))))
