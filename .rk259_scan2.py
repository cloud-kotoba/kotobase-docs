import io
t = io.open('query-cosientist.md', encoding='utf-8').read()
lines = t.splitlines()
# K-Z4 mentions with context
for i, l in enumerate(lines):
    if 'K-Z4' in l:
        print('LINE', i + 1)
        print(l[:1200])
        print('---')
# iteration log entries newer than rank258 entry (idx found earlier ~427+)
h = next(i for i, l in enumerate(lines) if l.strip() == '## Iteration log')
entries = [(i, l) for i, l in enumerate(lines) if i > h and l.startswith('- 2026')]
for i, l in entries[-4:]:
    print('ENTRY', i)
    print(l[:900])
    print('===')
