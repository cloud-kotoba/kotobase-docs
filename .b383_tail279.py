#!/usr/bin/env python3
# inspect K-Z3 evidence row (L279) tail to find append anchor.
line=open('query-cosientist.md',encoding='utf-8').read().split('\n')[278]
print("LEN of L279:", len(line))
print("TAIL 2500:")
print(line[-2500:])