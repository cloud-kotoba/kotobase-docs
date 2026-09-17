import unicodedata
p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
t=open(p,encoding='utf-8').read()
print('run558 count', t.count('run558'))
print('falsify 第248回 count', t.count('falsify 第248回'))
comb=[c for c in t if unicodedata.combining(c)]
print('combining chars', len(comb))
i=t.index('## Iteration log')
print('iter first row head:', repr(t[i:i+80]))
