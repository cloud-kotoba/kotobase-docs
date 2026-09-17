#!/usr/bin/env python3
import sys
p = 'query-cosientist.md'
data = open(p, 'rb').read()
# find K-Z3 row (line starting with '| K-Z3 | worker |')
marker = b'| K-Z3 | worker |'
idx = data.find(marker)
print('kz3_row_start', idx, file=sys.stderr)
# row end = position of newline after start
nl = data.find(b'\n', idx)
print('kz3_row_end_newline', nl, file=sys.stderr)
# tail after stripping
tail = data[idx:nl][-300:]
print('row_byte_len', nl - idx, file=sys.stderr)
print('ROWTAIL_START')
sys.stdout.buffer.write(tail + b'\nROWTailOK\n')
# Iteration log header
hdr = b'## Iteration log'
hi = data.find(hdr)
print('iter_header', hi, file=sys.stderr)
print('iter_header_start', hi, file=sys.stderr)