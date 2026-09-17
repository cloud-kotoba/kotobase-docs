import io

path = 'query-cosientist.md'
for i, line in enumerate(open(path, encoding='utf-8'), 1):
    s = line.rstrip('\n')
    if s.startswith('| K-Z') or s.startswith('| K-Q') or s.startswith('| K-S'):
        print(i, s[:80])
