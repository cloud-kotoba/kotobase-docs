import sys, os
out = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rank38_out14.txt','w')
sys.stdout = out
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
txt = open('query-cosientist.md', encoding='utf-8').read()
print('size:', len(txt.encode('utf-8')))
print('rank 第37回 block count:', txt.count('rank (期待 gain × 確率, 2026-09-05 第37回):'))
print('rank 第36回 block count (should be 0):', txt.count('rank (期待 gain × 確率, 2026-09-05 第36回):'))
print('log rank 第37回:', txt.count('- 2026-09-05: rank 第37回。'))
lines = txt.splitlines()
print('total lines:', len(lines))
print('=== TAIL 40 ===')
for l in lines[-40:]:
    print(l)
out.close()
