#!/usr/bin/env python3
# append evidence to line 279 (K-Z3 row) end.
import io
p = 'query-cosientist.md'
with io.open(p, encoding='utf-8') as f:
    lines = f.readlines()
if len(lines) < 279:
    print('ERR too short')
    raise SystemExit(1)
row = lines[278]
if 'K-Z3' not in row:
    print('ERR not K-Z3 row')
    print(row[:100])
    raise SystemExit(1)
with io.open('/tmp/run365_evidence.txt', encoding='utf-8') as g:
    adds = g.read()
lines[278] = row.rstrip('\n') + adds.rstrip('\n') + '\n'
with io.open(p, 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('APPENDED_OK rows=', len(lines))