#!/usr/bin/env python3
import re, sys
path = sys.argv[1] if len(sys.argv) > 1 else '.b189_run424_stats.py'
with open(path, 'r', encoding='utf-8', errors='ignore') as f:
    src = f.read()
# remove all combining diacritical marks
src = re.sub(r'[\u0300-\u036f]', '', src)
src = src.replace('Norme', 'None')
src = src.replace('Norm', 'None')
with open(path, 'w', encoding='utf-8') as f:
    f.write(src)
print('sanitized')