#!/usr/bin/env python3
fn = "query-cosientist.md"
s = open(fn, encoding="utf-8").read()
res = []
for c in set(s):
    o = ord(c)
    if (0x300 <= o <= 0x36f) or (0x200b <= o <= 0x200d) or (o == 0xfeff):
        res.append([c, hex(o), s.count(c)])
print(res)