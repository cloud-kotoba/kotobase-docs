#!/usr/bin/env python3
import re
data = open('query-cosientist.md', encoding='utf-8').read()
h = '## Iteration log\n'
i = data.find(h)
seg = data[i:i+9000]
for m in re.finditer(r'- \d{4}-\d{2}-\d{2}:\s*\*?(?:falsify|bench|cosientist|rank)[^\n]*', seg):
    print(m.group(0)[:200])
    print('---')