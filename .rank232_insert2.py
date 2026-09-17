path = 'query-cosientist.md'
entry = open('.rank232_entry.txt', encoding='utf-8').read().rstrip('\n')
wt = open(path, encoding='utf-8').read()

hdr = '## Iteration log\n'
idx = wt.find(hdr)
if idx < 0:
    raise SystemExit('ERROR: header not found')
pos = idx + len(hdr)
new_wt = wt[:pos] + entry + '\n\n' + wt[pos:]
open(path, 'w', encoding='utf-8').write(new_wt)
print('ok hdr_count=', new_wt.count('## Iteration log'))
print('entry inserted:', '第232回' in new_wt)