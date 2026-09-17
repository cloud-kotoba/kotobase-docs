#!/usr/bin/env python3
# -*- coding: utf-8 -*-
with open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(260, 273):
    h = lines[i][:28]
    print(f"LINE{i+1} head={h!r} len={len(lines[i])}")