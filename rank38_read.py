import sys
out = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rank38_out3.txt','w')
sys.stdout = out
import os
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
p = 'query-cosientist.md'
lines = open(p).read().splitlines()
print('TOTAL_LINES', len(lines))
# print hypotheses table region and last ~120 lines
start = None
for i,l in enumerate(lines):
    if 'K-' in l and ('|' in l) and start is None:
        start = max(0,i-3)
if start:
    print('=== from line', start+1)
    for l in lines[start:start+60]:
        print(l)
print('=== TAIL 100 ===')
for l in lines[-100:]:
    print(l)
out.close()
