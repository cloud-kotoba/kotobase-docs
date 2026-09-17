s = open('query-cosientist.md').read()
for r in ['run625', 'run624']:
    i = 0
    while True:
        i = s.find(r, i)
        if i < 0: break
        print('---', r, '@', i)
        print(s[max(0,i-160):i+200].replace('\n',' | '))
        i += 1
