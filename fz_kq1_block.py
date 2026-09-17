#!/usr/bin/env python3
txt = open("query-cosientist.md").read().splitlines()
# find K-Q1 block lines 52-75 (0-indexed 51-74), print each line's first 260 chars
for i in range(51, 75):
    if i < len(txt):
        print(f"L{i+1} (len {len(txt[i])}): {txt[i][:260]}")
print("<<END>>")
