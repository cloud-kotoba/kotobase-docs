txt = open('query-cosientist.md', encoding='utf-8').read()
i = txt.find('run458')
print(repr(txt[max(0,i-200):i+200]))