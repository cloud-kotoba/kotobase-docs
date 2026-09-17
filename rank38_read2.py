import sys
out = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rank38_out4.txt','w')
sys.stdout = out
import os
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
p = 'query-cosientist.md'
lines = open(p).read().splitlines()
# find rank block
for i,l in enumerate(lines):
    if 'rank' in l.lower() and ('第' in l) and ('block' in l.lower() or 'ブロック' in l):
        print(i+1, l[:200])
# Find the rank block section by searching for "rank ブロック"
idx = None
for i,l in enumerate(lines):
    if 'rank ブロック' in l and '第36回版' in l:
        idx = i
        print('FOUND at', i+1, l[:150])
if idx is None:
    # search for '## rank' heading
    for i,l in enumerate(lines):
        if l.startswith('#') and 'rank' in l.lower():
            print('HEADING', i+1, l[:100])
# also print lines 1-50
print('=== HEAD 55 ===')
for l in lines[:55]:
    print(l[:400])
out.close()
