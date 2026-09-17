import io, subprocess
out = io.open('/tmp/postpush.txt', 'w', encoding='utf-8')

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    return (r.returncode, r.stdout, r.stderr)

rc, so, se = run(['git','fetch','bench_fetch'])
out.write('fetch rc=%d %s %s\n' % (rc, so[:150], se[:150]))
rc, so, se = run(['git','rev-parse','bench_fetch/main'])
out.write('remote main: %s\n' % so.strip())
rc, so, se = run(['git','log','--oneline','-3','bench_fetch/main'])
out.write('remote log:\n%s\n' % so)
# verify my entry present in remote HEAD blob
rc, so, se = run(['git','show','bench_fetch/main:query-cosientist.md'])
content = so
hc = content.count('## Iteration log')
has_rank204 = 'rank 第204回' in content
out.write('remote header count: %d\n' % hc)
out.write('remote has rank 第204回: %s\n' % has_rank204)
#, check my entry is top of iter log
lines = content.split('\n')
for i,l in enumerate(lines):
    if l.startswith('- 2026-09-08:'):
        out.write('remote ILOG %d: %s\n' % (i+1, l[:60]))
        break
out.close()
print('done')