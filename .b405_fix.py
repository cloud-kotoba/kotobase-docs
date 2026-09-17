#!/usr/bin/env python3
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b405_insert.py"
s = open(p, encoding="utf-8").read()
bad = "\u4f46\u3057 ran \u7d9a\u304d"
good = "\u4f46\u3057 run \u7d9a\u304d"
# NOTE: in the source file the escapes are literal backslash-u sequences, not decoded chars.
src = open(p, "rb").read()
badb = b"ran \\u7d9a"
goodb = b"run \\u7d9a"
cnt = src.count(badb)
src = src.replace(badb, goodb)
open(p, "wb").write(src)
print("replaced", cnt)
