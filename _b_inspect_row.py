#!/usr/bin/env python3
# -*- coding: utf-8 -*-
with open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("total lines:", len(lines))
for i in [259, 260, 265, 266, 267, 268, 269, 270]:
    if i < len(lines):
        print(f"LINE {i+1} len={len(lines[i])} head30={lines[i][:30]!r} tail40={lines[i][-40:]!r}")
print("---")
print("LINE268 contains run271A-C:", 'run271A-C' in lines[267])
print("LINE268 tail:", repr(lines[267][-120:]))