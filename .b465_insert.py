#!/usr/bin/env python3
import sys

p = 'query-cosientist.md'
data = open(p, 'rb').read()

def scrub(b):
    s = b.decode('utf-8')
    for ch in ['\u200b', '\u200c', '\u200d', '\ufeff']:
        s = s.replace(ch, '')
    s = s.replace('#####', '')
    return s.encode('utf-8')

ev = scrub(open('.b465_ev.txt', 'rb').read()).rstrip(b'\n')
ilog = scrub(open('.b465_ilog.txt', 'rb').read()).rstrip(b'\n')

marker = b'| K-Z3 | worker |'
row_start = data.find(marker)
row_nl = data.find(b'\n', row_start)
print('row_start', row_start, 'row_nl', row_nl, file=sys.stderr)

hdr = b'## Iteration log\n'
hi = data.find(hdr)
iter_insert = hi + len(hdr)
print('iter_header', hi, 'iter_insert', iter_insert, file=sys.stderr)

# 1) iter entry (HIGH offset) first
data2 = data[:iter_insert] + ilog + b'\n' + data[iter_insert:]

# 2) evidence at LOW offset (row_nl unchanged)
data3 = data2[:row_nl] + b' ' + ev + data2[row_nl:]

open(p, 'wb').write(data3)
print('WROTE', len(data3), file=sys.stderr)
print('OK_DONE')