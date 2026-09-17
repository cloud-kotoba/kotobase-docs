import re
txt = open('query-cosientist.md', encoding='utf-8').read()
print('len', len(txt))
print('iterlog headers', txt.count('## Iteration log'))
i = txt.index('## Iteration log')
print('--- first 900 chars after iterlog ---')
print(txt[i:i+900])
# K-Z3 row
m = re.search(r'^\| K-Z3 \|.*$', txt, re.M)
print('--- K-Z3 row tail 1500 ---')
print(m.group(0)[-1500:])
# K-Z4 rows
for mm in re.finditer(r'^\| K-Z4 \|.*$', txt, re.M):
    print('--- K-Z4 row head 400 ---')
    print(mm.group(0)[:400])
