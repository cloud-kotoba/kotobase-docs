#!/usr/bin/env python3
# -*- coding: utf-8 -*-
with open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(267, 272):
    print(f"LINE{i+1} head={lines[i][:50]!r} len={len(lines[i])}")
print("---")
print("run272 present in line 269:", 'run272A-C' in lines[268])
print("run271 still in line 268:", 'run271A-C' in lines[267])