#!/usr/bin/env python3
d = open('query-cosientist.md', encoding='utf-8').read()
import re
# find run424 occurrences with context
for m in re.finditer(r'run424', d):
    s = max(0, m.start()-120)
    e = min(len(d), m.end()+220)
    print('>>>', d[s:e].replace('\n', ' ')[:340])
    print()