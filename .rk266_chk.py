import re
p = 'query-cosientist.md'
s = open(p, encoding='utf-8').read()
hdr = '## Iteration log'
# occurrences that are at line start
line_starts = len(re.findall(r'(?m)^## Iteration log$', s))
print('line-start hdr:', line_starts)
anchor = hdr + '\n\n- 2026-09-13: bench 第269回'
print('anchor1:', s.count(anchor))
anchor2 = hdr + '\n- 2026-09-12 (本 tick, K-Z3 23時台'
print('anchor2:', s.count(anchor2))
# where do the extra headers sit
for m in re.finditer(r'## Iteration log', s):
    line_no = s.count('\n', 0, m.start()) + 1
    print('occ line', line_no)
