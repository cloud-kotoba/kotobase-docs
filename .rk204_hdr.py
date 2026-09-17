import io
p = 'query-cosientist.md'
txt = io.open(p, encoding='utf-8').read()
lines = txt.split('\n')
out = io.open('/tmp/hdr.txt', 'w', encoding='utf-8')
# rank ordering header (line 135 area)
for i, l in enumerate(lines):
    if l.startswith('rank (期待 gain'):
        out.write('RANKHDR line %d: %s\n' % (i+1, l[:400]))
        break
# rank 第204回 existing?
for i, l in enumerate(lines):
    if 'rank 第204回' in l:
        out.write('EXISTS rank204 line %d\n' % (i+1))
# iter-log top 4 entries (find first 4 lines starting with '- 2026-09-08')
cnt = 0
for i, l in enumerate(lines):
    if l.startswith('- 2026-09-08:'):
        head = l[:90]
        out.write('ILOG %d: %s\n' % (i+1, head))
        cnt += 1
        if cnt >= 5:
            break
out.write('header count: %d\n' % txt.count('## Iteration log'))
out.close()
print('ok')
