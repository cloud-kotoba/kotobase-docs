#!/usr/bin/env python3
import re
p='query-cosientist.md'
lines=open(p,encoding='utf-8').read().split('\n')

# identify marker lines that are DUPLICATE iter-log entries for falsify 175
# keep the FIRST one (the newest, right after header); remove all other iter-log entry lines
# starting with "- 2026-09-07: **falsify 第175回**" (the full entry lines only, not L279 evidence)
keep=None; drop=[]
for i,l in enumerate(lines):
    if re.match(r'^-\s+2026-09-07:\s*\*\*falsify\s+第175回\*\*', l):
        if keep is None:
            keep=i
        else:
            drop.append(i)

assert keep is not None, 'no falsify175 entry found'
out=[lines[i] for i in range(len(lines)) if i not in set(drop)]
open(p,'w',encoding='utf-8').write('\n'.join(out))
print('kept line', keep+1, 'dropped lines', [d+1 for d in drop])