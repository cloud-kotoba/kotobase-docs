import io
NL = '\n'
p = 'query-cosientist.md'
s = io.open(p, encoding='utf-8').read()
# Fix 1: re-add newline + run229 closer before glued run230
a1 = '深夜帯 ~26-31% 平坦パターンとの対比も維持。falsify 2026-09-06 (第100回'
b1 = '深夜帯 ~26-31% 平坦パターンとの対比も維持。status 判定は rank に委ねる (rank 専門)。' + NL + 'falsify 2026-09-06 (第100回'
assert s.count(a1) == 1, 'a1 cnt=%d' % s.count(a1)
s = s.replace(a1, b1, 1)
# Fix 2: remove the stray status line before Iteration log
a2 = 'rank 専門)。' + NL + 'status 判定は rank に委ねる (rank 専門)。' + NL + NL + '## Iteration log'
b2 = 'rank 専門)。' + NL + NL + '## Iteration log'
assert s.count(a2) == 1, 'a2 cnt=%d' % s.count(a2)
s = s.replace(a2, b2, 1)
io.open(p, 'w', encoding='utf-8').write(s)
print('fixed ok')