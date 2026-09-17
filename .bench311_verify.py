#!/usr/bin/env python3
lines = open('query-cosientist.md', encoding='utf-8').read().split('\n')
ln = lines[278]
print("K-Z3 row? ", ln.startswith('| K-Z3 | worker |'))
print("run311 present:", 'run311A–C' in ln)
print("len:", len(ln))
print("TAIL:", ln[-180:])
# secret scan
import re
for pat in ['Bearer','token=','password','secret','-----BEGIN','0x[a-f0-9]{64}','cookie']:
    if pat.lower() in ln.lower():
        # crude locate
        idx = ln.lower().find(pat.lower())
        print("POSSIBLE SECRET TOKEN:", pat, "at", idx, "ctx:", ln[max(0,idx-30):idx+60])