data = open('query-cosientist.md', encoding='utf-8').read()
lines = data.split(chr(10))
found = []
for i in range(len(lines)):
    line = lines[i]
    if 'K-Z1/K-Z2' in line and len(line) > 1000:
        found.append((i+1, len(line)))
    if line.strip() == '## Iteration log':
        found.append(('ITER', i+1, lines[i+1][:40]))
for f in found:
    print(f)
print('total_lines', len(lines))