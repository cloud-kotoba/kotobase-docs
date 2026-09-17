#!/usr/bin/env python3
# -*- coding: utf-8 -*-
SRC = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
with open(SRC, 'r', encoding='utf-8') as f:
    txt = f.read()
old = "機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門).\n"
new = "機構判断には rank 追加 n を要する。status 判定は rank に委ねる (rank 専門)。\n"
assert txt.count(old) == 1, "anchor not unique"
txt = txt.replace(old, new)
with open(SRC, 'w', encoding='utf-8') as f:
    f.write(txt)
print("fixed trailing period; confirm endash run272 still present:", 'run272A\u2013C' in txt)