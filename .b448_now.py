#!/usr/bin/env python3
import subprocess
def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True, cwd='.')
    open('/tmp/b448_now.log','a').write('$ ' + ' '.join(cmd) + '\n' + (r.stdout or '') + '\n')
for c in [['git','log','--oneline','-4'],
          ['git','rev-parse','HEAD'],
          ['git','rev-parse','net-kotobase/main'],
          ['git','status','--short','query-cosientist.md']]:
    run(c)
print('ok')