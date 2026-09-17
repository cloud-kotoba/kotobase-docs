#!/usr/bin/env python3
import os
base = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
md = os.path.join(base, 'query-cosientist.md')
with open(md, 'r', encoding='utf-8') as f:
    c = f.read()
old = 'HEAD <push後確認>'
new = 'HEAD f2508c1 = remote net-kotobase/main (push 後一致,'
assert c.count(old) == 1, ('target count', c.count(old))
c = c.replace(old, new)
with open(md, 'w', encoding='utf-8') as f:
    f.write(c)
print('OK')