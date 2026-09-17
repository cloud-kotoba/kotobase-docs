#!/usr/bin/env python3
import re
for src, dst in [('/tmp/f_ev415.txt','/tmp/f_ev415c.txt'),('/tmp/f_il415.txt','/tmp/f_il415c.txt')]:
    t = open(src, encoding='utf-8').read()
    t = t.replace('\u200b','').replace('\u200c','').replace('\u200d','')
    open(dst, 'w', encoding='utf-8').write(t)
    print(dst, 'len', len(t))