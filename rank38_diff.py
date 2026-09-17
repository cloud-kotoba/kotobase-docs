import sys
out = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rank38_out7.txt','w')
sys.stdout = out
import subprocess, os
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
for cmd in [
    ['git','diff','--stat','--','query-cosientist.md'],
    ['git','diff','--','query-cosientist.md'],
    ['git','status','--short','--','query-cosientist.md'],
]:
    r = subprocess.run(cmd, capture_output=True, text=True)
    print('$', ' '.join(cmd), '->', r.returncode)
    print(r.stdout[-6000:])
    if r.stderr: print('STDERR:', r.stderr[-300:])
out.close()
