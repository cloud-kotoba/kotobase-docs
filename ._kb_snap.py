# -*- coding: utf-8 -*-
import io, subprocess
r = subprocess.run(['git','status','--short'], capture_output=True, text=True, cwd='.')
tracked = [l for l in r.stdout.splitlines() if not l.startswith('??')]
out = []
out.append('TRACKED:')
out.extend(tracked)
d = subprocess.run(['git','diff','--stat','--','query-cosientist.md'], capture_output=True, text=True)
out.append('DIFFSTAT:')
out.append(d.stdout.strip())
out.append('RUN499COUNT:'+sum)
# count run499
with io.open('query-cosientist.md', encoding='utf-8') as f:
    data = f.read()
out.append('RUN499COUNT=%d' % data.count('run499'))
out.append('NTH218=%d' % data.count('bench 第218回'))
out.append('SEPARATOR_LINES=%d' % data.count('\n## Iteration log\n'))
with io.open('/tmp/kb_sn.txt','w',encoding='utf-8') as f:
    f.write('\n'.join(out)+'\n')
print('done')