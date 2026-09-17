path = 'query-cosientist.md'
lines = open(path, encoding='utf-8').readlines()
for i in range(205, 212):
    s = lines[i].rstrip('\n')
    print(i + 1, repr(s[-80:]))
