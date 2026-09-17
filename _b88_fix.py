import re
p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
s=open(p).read()
old='14時台通算は 9/5 run152 (5/60 ~8.3%) + 本 tick (1/60) で 6/120 (~5%) の低位帯寄り'
assert s.count(old)==1, s.count(old)
new='14時台通算は 9/5 run152 (5/60 ~8.3%) + falsify 第86回 run212 (4/60, 14:06 同時刻帯の並行計測, 本 commit に同乗) + 本 tick (1/60) で 10/180 (~5.6%) の低位帯寄り'
s=s.replace(old,new)
open(p,'w').write(s)
print('PATCHED')
