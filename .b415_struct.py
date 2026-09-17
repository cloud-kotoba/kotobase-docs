#!/usr/bin/env python3
lines = open('query-cosientist.md', encoding='utf-8').read().split('\n')
for i in range(274, 285):
    s = lines[i]
    head = s[:30]
    print(i+1, len(s), head)