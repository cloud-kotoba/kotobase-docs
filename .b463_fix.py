#!/usr/bin/env python3
p = 'query-cosientist.md'
data = open(p, 'rb').read()
old = 'host load1 20.89 (09:0? uptime 実測 → 12:20 12:20:00, gate 7.5 大幅超過)'
new = 'host load1 20.89 (pre-run uptime 実測, gate 7.5 大幅超過)'
ob = old.encode('utf-8')
nb = new.encode('utf-8')
n = data.count(ob)
print('count', n)
if n == 1:
    data = data.replace(ob, nb)
    open(p, 'wb').write(data)
    print('REPLACED')
else:
    print('NOT_UNIQUE_OR_MISSING')