import io
lines = io.open('query-cosientist.md', encoding='utf-8').read().splitlines()
for i, l in enumerate(lines):
    if l.startswith('| K-S1') or l.startswith('| K-Z3') or l.startswith('| K-Z2'):
        print('ROW', i + 1, l[:160])
print('headers:', [i + 1 for i, l in enumerate(lines) if l.strip() == '## Iteration log'])
# last evidence line for K-Z3 (row ending) - print tail of first K-Z3 row
