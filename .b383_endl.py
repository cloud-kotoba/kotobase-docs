#!/usr/bin/env python3
line=open('query-cosientist.md',encoding='utf-8').read().split('\n')[278]
print("LAST 400 chars of L279:")
print(repr(line[-400:]))