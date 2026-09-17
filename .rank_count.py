s=open('query-cosientist.md',encoding='utf-8').read()
c=s.count('## Iteration log')
print('count',c)
start=0
for _ in range(c):
    i=s.find('## Iteration log',start)
    print(i, repr(s[i:i+60]))
    start=i+1