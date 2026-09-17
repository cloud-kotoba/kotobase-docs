import io
NL = '\n'
p = 'query-cosientist.md'
s = io.open(p, encoding='utf-8').read()
a = NL + ' JST tick (pre-run 計測 18:02'
b = NL + '- 2026-09-06: rank 第97回。18:02 JST tick (pre-run 計測 18:02'
assert s.count(a) == 1, 'a cnt=%d' % s.count(a)
s = s.replace(a, b, 1)
io.open(p, 'w', encoding='utf-8').write(s)
print('restored rank97 header ok')