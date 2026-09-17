src = open('query-cosientist.md', encoding='utf-8').read()
i = src.find('falsify 2026-09-05 (第63回')
assert i != -1
k = src.find('\n|', i)
# K-Z3 row: find segment between 第63回 evidence start and end of row
# print the evidence fragment to inspect
print(repr(src[i:i+700]))
