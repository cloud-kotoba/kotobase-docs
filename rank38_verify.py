import sys
out = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rank38_out10.txt','w')
sys.stdout = out
import os
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
data = open('query-cosientist.md','rb').read()
print('bytes:', len(data))
txt = data.decode('utf-8')
for key in ['cosientist 第9回','bench 第37回','falsify 2026-09-05 (K-Z2 発火直後','rank 第36回','NEXT (rank 第36回) の K-Z2']:
    print(key, '->', txt.count(key))
lines = txt.splitlines()
print('lines:', len(lines))
print('LAST LINE:', lines[-1][:300])
out.close()
