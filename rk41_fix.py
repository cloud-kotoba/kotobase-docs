import io
p = 'query-cosientist.md'
s = io.open(p, encoding='utf-8').read()
a = '6時台通算 20 試行中 3 試行 (~15%)'
b = '6時台通算 15 試行中 2 試行 (~13%)'
assert a in s, 'rank block pattern not found'
s = s.replace(a, b)
c = 'falsify run118 で 20 試行中 3 試行\n  ~15%)'
d = 'falsify run118 で 15 試行中 2 試行\n  ~13% — cold>0 は run105A と run116A の 2 run)'
assert c in s, 'log pattern not found'
s = s.replace(c, d)
io.open(p, 'w', encoding='utf-8').write(s)
print('FIXED')
