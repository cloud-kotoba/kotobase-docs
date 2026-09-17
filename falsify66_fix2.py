p = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
t = open(p).read()
assert 'rank 尚門' in t
t = t.replace('rank 尚門', 'rank 専門')
open(p, 'w').write(t)
print('fixed')
