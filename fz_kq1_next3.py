#!/usr/bin/env python3
txt = open("query-cosientist.md").read().splitlines()
for i in range(61, 80):
    if i < len(txt):
        print(f"L{i+1}: {txt[i][:220]}")
print("<<END>>")
