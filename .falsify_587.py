import re
txt = open('query-cosientist.md', encoding='utf-8').read()
# find run587 context: what URLs were measured? look around mentions of run587
i = txt.find('run587A')
while i != -1:
    print('---CTX---')
    print(txt[max(0,i-600):i+200].replace('\n',' | ')[-800:])
    i = txt.find('run587A', i+1)
    if i > 10**7: break
