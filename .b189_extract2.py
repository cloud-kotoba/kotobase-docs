import re
lines = open('.b189_qc_base.md').read().split('\n')
start = None
for i, l in enumerate(lines):
    if l.startswith('| K-Z3 |'):
        start = i
        break
if start is None:
    print('K-Z3 row not found')
    raise SystemExit
end = len(lines)
for j in range(start + 1, len(lines)):
    l = lines[j]
    if l.startswith('| ') and re.match(r'\|\s*K-', l)and not l.startswith('| K-Z3'):
        end = j
        break
print('kz3_row_start', start, 'end', end, 'lenspan', end - start)
print('---TAIL 8---')
for l in lines[end-8:end]:
    print(l[:3000])
print('---CONTEXT AFTER ROW---')
if end < len(lines):
    print(lines[end][:200])