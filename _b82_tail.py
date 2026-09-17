with open('query-cosientist.md', encoding='utf-8') as f:
    text = f.read()
row = text[text.find('| K-Z3 '):]
end = row.find('\n')
row = row[:end]
print('row len', len(row))
print('TAIL 700:')
print(row[-700:])
