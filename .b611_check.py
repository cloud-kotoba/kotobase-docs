import re
p = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
s = open(p, encoding='utf-8').read()
# count occurrences of unique markers
for m in ['falsify 2026-09-14 (第250回, K-Z3 3時台帯初 run611A-C', '3時台通算 (9/11 run578 10/60 + 9/14 本測 11/60)']:
    print(m[:40], s.count(m))
# combining-char scan
bad = sorted({c for c in s if 0x0300 <= ord(c) <= 0x036F})
print('combining chars:', [hex(ord(c)) for c in bad])
# iter header count
print('iter headers:', s.count('\n## Iteration log\n'))
