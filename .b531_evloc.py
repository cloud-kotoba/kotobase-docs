lines = open('query-cosientist.md', encoding='utf-8').read().split('\n')
n = len(lines)
L = lines[278]  # 0-indexed -> line 279
tail = L[-160:]
print('line279_len', len(L))
print('tail>>>' + repr(tail))
print('has_zwnbsp', '\u200b' in L)
print('total_lines', n)