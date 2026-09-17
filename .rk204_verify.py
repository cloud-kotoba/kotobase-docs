import io, subprocess
p = 'query-cosientist.md'
out = io.open('/tmp/verify2.txt', 'w', encoding='utf-8')
txt = io.open(p, encoding='utf-8').read()
hc = txt.count('## Iteration log')
out.write('header count: %d\n' % hc)
lines = txt.split('\n')
cnt = 0
for i, l in enumerate(lines):
    if l.startswith('- 2026-09-08:'):
        out.write('ILOG %d: %s\n' % (i+1, l[:70]))
        cnt += 1
        if cnt >= 4:
            break
# numstat
r = subprocess.run(['git','diff','HEAD','--numstat','--','query-cosientist.md'],
                   capture_output=True, text=True)
out.write('numstat: %r\n' % r.stdout)
r2 = subprocess.run(['git','rev-parse','HEAD'], capture_output=True, text=True)
out.write('HEAD: %s\n' % r2.stdout.strip())
out.close()
print('ok')