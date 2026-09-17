#!/usr/bin/env python3
txt = open("query-cosientist.md").read().splitlines()
# print lines 52-56
for i in range(51, 56):
    print(f"L{i+1}: {txt[i][:200]}")
print("<<END>>")
