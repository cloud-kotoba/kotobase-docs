import io
t = io.open('query-cosientist.md', encoding='utf-8').read()
print('K-Z4 count', t.count('K-Z4'))
for l in t.splitlines():
    if l.startswith('| K-Z4'):
        print(l[:600])
print('---rank258 NEXT---')
for l in t.splitlines():
    if 'run578' in l:
        print(l[:400])
