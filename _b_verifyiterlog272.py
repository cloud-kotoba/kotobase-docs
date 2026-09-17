#!/usr/bin/env python3
# -*- coding: utf-8 -*-
with open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print("LINE316:", repr(lines[315][:60]))
print("LINE317:", repr(lines[316][:60]))
print("checking run272 iterlog present:", '第110回' in lines[315])
print("checking run272 evidence present:", 'run272A\u2013C' in ''.join(lines[267:270]))