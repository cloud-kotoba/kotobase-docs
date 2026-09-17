import sys
out = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rank38_out12.txt','w')
sys.stdout = out
import os
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
txt = open('query-cosientist.md', encoding='utf-8').read()
lines = txt.splitlines()
# print lines 148-152 fully (the K-Z2 run106/run107 evidence)
for i in range(147, 153):
    print('LINE', i+1, ':', lines[i][:1200])
    print('---')
out.close()
