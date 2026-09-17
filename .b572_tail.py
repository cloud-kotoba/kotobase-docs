#!/usr/bin/env python3
p='query-cosientist.md'
for l in open(p).read().split('\n'):
    if l.startswith('| K-Z3 |'):
        print(repr(l[-300:]))
