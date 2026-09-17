#!/usr/bin/env python3
fn = "query-cosientist.md"
s = open(fn, encoding="utf-8").read()
for o in range(768,880):
    s = s.replace(chr(o),"")
for o in range(8203,8206):
    s = s.replace(chr(o),"")
s = s.replace(chr(65279),"")
open(fn,"w",encoding="utf-8").write(s)
print("done")