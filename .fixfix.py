#!/usr/bin/env python3
p='.b189_evidence.py'
with open(p,'r',encoding='utf-8') as f:
    s=f.read()
s=s.replace("join(lines\n","join(lines)\n")
s=s.replace("write(frag\n","write(frag)\n")
with open(p,'w',encoding='utf-8') as f:
    f.write(s)