import io, subprocess, re

docs = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/'
src = docs + 'query-cosientist.md'

def sh(cmd):
    p = subprocess.run(cmd, shell=True, cwd=docs, capture_output=True, text=True)
    return (p.stdout or '') + (p.stderr or '')

log = []
log.append('HEAD=' + sh('git rev-parse HEAD').strip())

with io.open(src, encoding='utf-8') as f:
    t = f.read()

# locate K-Z3 row
kz3 = t.find('\n| K-Z3 |')
log.append('kz3 row idx=%d' % kz3)
seg_start = kz3
seg_end = t.find('\n| K-S', kz3 + 1)
log.append('seg_end=%d' % seg_end)
seg = t[seg_start:seg_end]
log.append('seg len=%d, run211=%d, run210=%d, 211A=%d' % (len(seg), seg.count('run211'), seg.count('run210'), seg.count('211A')))
log.append('seg tail 200: ' + seg[-200:])

with io.open('/tmp/_f86_diag2.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(log) + '\n')
