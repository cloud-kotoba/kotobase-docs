#!/usr/bin/env python3
# -*- coding: utf-8 -*-
with open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print("iterlog 第110回 at line317:", '第110回' in lines[316])
print("run273 NEXT present:", 'run273' in lines[316])
print("run272 present in iterlog:", 'run272A\u2013C' in lines[316])