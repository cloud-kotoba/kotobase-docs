#!/usr/bin/env python3
path = 'query-cosientist.md'
with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
kz3 = [ln for ln in lines if ln.startswith('| K-Z3 |')]
print('kz3 rows=', len(kz3))
row = kz3[0]
print('row run521 count=', row.count('run521'))
print('row 第232回 count=', row.count('第232回'))
print('row ends with run521 evidence=', row.rstrip().endswith('status 判定は rank に委ねる (rank 専門)。'))
print('row tail=', repr(row[-300:]))
allt = ''.join(lines)
print('wholefile run521 count=', allt.count('run521'))
print('wholefile 第232回 count=', allt.count('第232回'))
print('wholefile falsify 第232回。01:37 count=', allt.count('falsify 第232回。01:37 JST tick'))