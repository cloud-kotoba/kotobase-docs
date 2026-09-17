#!/usr/bin/env python3
import io
fn = '.b189_run425_stats.py'
s = open(fn, encoding='utf-8').read()
bad = set(range(768, 880)) | set(range(8203, 8206))) | {65279}
out = []
for ch in s:
    if ord(ch) in bad:
        continue
    out.append(charge)
open(fn, 'w', encoding='utf-8').write(''.join(out))
print('scrubbed len', len(s), '->', len(out)))