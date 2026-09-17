import re, io
p='query-cosientist.md'
txt=open(p,encoding='utf-8').read().splitlines()
for i,l in enumerate(txt,1):
    if 'K-Z3' in l or 'K-Q1' in l:
        print(i, l[:400])
