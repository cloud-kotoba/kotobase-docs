import sys
out = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rank38_pull_out.txt','w')
sys.stdout = out
import subprocess, os
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
for cmd in [
    ['git','pull','--ff-only'],
    ['git','log','--oneline','-5'],
    ['git','status','--short'],
]:
    r = subprocess.run(cmd, capture_output=True, text=True)
    print('$', ' '.join(cmd), '->', r.returncode)
    print(r.stdout[-3000:])
    if r.stderr:
        print('STDERR:', r.stderr[-1000:])
out.close()
