#!/usr/bin/env python3
# -*- coding: utf-8 -*-
with open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()
print("run272A-C (hyphen) in line269:", 'run272A-C' in lines[268])
print("run272A\u2013C (endash) in line269:", 'run272A\u2013C' in lines[268])
print("line269 full new_entry:", repr(lines[268][:80]))
# check tail
print("line269 tail:", repr(lines[268][-50:]))