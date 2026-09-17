#!/usr/bin/env python3
txt = open("query-cosientist.md").read().splitlines()
for i in range(74, 77):
    if i < len(txt):
        print(f"L{i+1} (len {len(txt[i])}):")
        print(txt[i])
        print("---")
print("<<END>>")
