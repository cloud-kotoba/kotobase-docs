p = 'query-cosientist.md'
s = open(p, encoding='utf-8').read()
needle = 'run128A'
idx = s.find(needle)
# find the K-Z3 row containing it
line_no = s[:idx].count('\n') + 1
lines = s.split('\n')
row = lines[line_no - 1]
out = open('/tmp/app128_check.txt', 'w', encoding='utf-8')
out.write(f'line {line_no}, row len {len(row)}\n')
out.write('...tail: ' + row[-400:] + '\n')
out.close()
print('ok')
