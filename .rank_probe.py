import re
s=open('query-cosientist.md',encoding='utf-8').read()
m=re.search(r'## Iteration log(.{0,70})',s,re.S)
print(repr(m.group(0)) if m else 'no')
i=s.find('## Iteration log')
print(repr(s[i:i+70]))