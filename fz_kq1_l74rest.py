#!/usr/bin/env python3
txt = open("query-cosientist.md").read().splitlines()
# L74 is 0-indexed 73
print(txt[73][260:1518])
print("<<END>>")
