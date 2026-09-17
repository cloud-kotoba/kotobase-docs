s=open('query-cosientist.md','rb').read().decode('utf8')
i=s.find('| K-Z3 | worker |')
nend=s.find('\n',i)
line=s[i:nend]
print('LEN',len(line))
print('CELL_END',repr(line[-120:]))
# locate iter log header
k=s.find('\n## Iteration log')
print('ITERPOS',k)
h=s.find('# Iteration log')
a=s.find('\n',h) if h>=0 else -1
print('ITER_LINE_END',repr(s[h:a+1] if a>=0 else '?'))