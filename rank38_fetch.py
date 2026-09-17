import sys
out = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rank38_out2.txt','w')
sys.stdout = out
import subprocess, os
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
for cmd in [
    ['git','fetch','net-kotobase'],
    ['git','rev-parse','net-kotobase/main'],
    ['git','log','--oneline','-3','net-kotobase/main'],
]:
    r = subprocess.run(cmd, capture_output=True, text=True)
    print('$', ' '.join(cmd), '->', r.returncode)
    print(r.stdout[-1500:])
    if r.stderr: print('STDERR:', r.stderr[-500:])
out.close()
