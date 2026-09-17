import re
p = 'query-cosientist.md'
s = open(p, encoding='utf-8').read()
hdr = '## Iteration log'
# remove the second line-start header (line ~434) preceded entry line
pat = re.compile(r'(?m)^## Iteration log\n(?=- 2026-09-12)', )
m = pat.findall(s)
print('pat matches:', len(m))
