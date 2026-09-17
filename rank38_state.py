import sys
out = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rank38_out.txt','w')
sys.stdout = out
import subprocess, os
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
for cmd in [
    ['git','branch','-a'],
    ['git','rev-parse','HEAD'],
    ['git','fetch','origin'],
    ['git','rev-parse','origin/main'],
    ['git','status'],
]:
    r = subprocess.run(cmd, capture_output=True, text=True)
    print('$', ' '.join(cmd), '->', r.returncode)
    print(r.stdout[-2000:])
    if r.stderr: print('STDERR:', r.stderr[-500:])
out.close()
