p = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
text = open(p).read()
check1 = 'run193A–C' in text
check2 = text.count('run193A–C') == 1
# also verify K-Z3 line integrity: table row still has one trailing status cell
lines = text.split('\n')
idx = -1
for i, ln in enumerate(lines):
    if ln.startswith('| K-Z3 |'):
        idx = i
line = lines[idx]
check3 = line.count('|') >= 5
print('found:', check1, 'unique:', check2, 'line_pipes_ok:', check3, 'line_len:', len(line))
