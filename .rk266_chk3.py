p = 'query-cosientist.md'
lines = open(p, encoding='utf-8').read().split('\n')
for ln in (433, 434, 435, 442, 443, 444):
    print(ln, '|', lines[ln-1][:120])
