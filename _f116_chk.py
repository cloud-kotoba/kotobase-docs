p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
t=open(p,encoding='utf-8').read()
m=t.count("falsify 2026-09-06 (第116回")
out="第116回 block: %d\n"%m
# find current NEXT line
import re
nxt=[l for l in t.split('\n') if 'NEXT:' in l]
out+="NEXT lines with 22時台: %d\n"%sum(1 for l in nxt if '22時台' in l)
open('/tmp/kz3_chk.txt','w',encoding='utf-8').write(out)
print("OK")