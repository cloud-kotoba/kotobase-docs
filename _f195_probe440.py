#!/usr/bin/env python3
s=open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md',encoding='utf-8').read()
import re
for m in re.finditer(r'run440', s):
    a=max(0,m.start()-80); b=min(len(s),m.end()+80)
    print(repr(s[a:b]))