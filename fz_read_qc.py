import sys
p = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
lines = open(p, encoding='utf-8').read().splitlines()
out = open('/tmp/qc_head.txt', 'w', encoding='utf-8')
for i, l in enumerate(lines[:120], 1):
    out.write(f'{i}|{l}\n')
out.close()
# also locate hypothesis rows
out2 = open('/tmp/qc_hits.txt', 'w', encoding='utf-8')
for i, l in enumerate(lines, 1):
    if 'K-Z3' in l or 'K-Z2' in l or 'K-Q1' in l or 'K-S1' in l or 'K-S2' in l:
        out2.write(f'{i}|{l[:200]}\n')
out2.close()
print('ok')
