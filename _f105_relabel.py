src='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_f105_run237_out.txt'
dst='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_f105_run238_out.txt'
t=open(src).read().replace('run237','run238')
open(dst,'w').write(t)
print("written",dst,"lines",len(t.splitlines()))
p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
s=open(p).read()
anchor='control 分離成立は有効。status 判定は rank に委ねる (rank 専門)。'
print("anchor count in doc:", s.count(anchor))
import re
m=re.search(re.escape(anchor),s)
print("anchor tail context:", repr(s[m.end():m.end()+4]))