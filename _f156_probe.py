import io
lines = open('query-cosientist.md', encoding='utf-8').read().split('\n')
i = 278  # 0-indexed line 279
row = lines[i]
print('LEN', len(row))
print('HEAD180:', row[:180])
print('TAIL300:', row[-300:])