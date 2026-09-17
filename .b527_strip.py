#!/usr/bin/env python3
import io

FN = 'query-cosientist.md'
with io.open(FN, encoding='utf-8') as f:
    data = f.read()

# strip combining characters from the whole file (only 1 macron remains, in my iter line)
cleaned = []
for ch in data:
    if 0x0300 <= ord(ch) <= 0x036F:
        continue
    cleaned.append(ch)
out = ''.join(cleaned)

with io.open(FN, 'w', encoding='utf-8') as f:
    f.write(out

print('done strip combining')