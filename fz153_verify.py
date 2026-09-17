src = open('query-cosientist.md').read()
i = src.find('| K-Z3')
print(src[i:i+900])
