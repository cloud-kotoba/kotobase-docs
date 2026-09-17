#!/usr/bin/env python3
lines = open('query-cosientist.md', encoding='utf-8').read().split('\n')
ln = lines[278]  # line 279
print("len", len(ln))
print("last 120 repr:", repr(ln[-120:]))
print("ends with '|':", ln.rstrip().endswith('|'))