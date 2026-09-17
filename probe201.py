import io
c=io.open('query-cosientist.md',encoding='utf-8').read()
i=c.index('## Iteration log')
print(c[i:i+2800])