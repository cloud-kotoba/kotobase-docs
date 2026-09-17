#!/usr/bin/env python3
with open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md', encoding='utf-8') as f:
    lines = f.readlines()
print("totallines", len(lines))
kz3 = [i for i,l in enumerate(lines) if l.startswith('| K-Z3 |')]
print("kz3_rows", kz3)
r = kz3[0]
print("--- K-Z3 row last 500 chars, repr ---")
print(repr(lines[r][-500:]))
print("--- tail of file ---")
for l in lines[-6:]:
    print(repr(l[:200]))