import sys
out = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rank38_out5.txt','w')
sys.stdout = out
import subprocess, os
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
for cmd in [
    ['git','fetch','net-kotobase'],
    ['git','log','--oneline','-5','net-kotobase/main'],
    ['git','rev-parse','HEAD'],
    ['git','rev-parse','net-kotobase/main'],
    ['git','diff','HEAD','net-kotobase/main','--stat'],
]:
    r = subprocess.run(cmd, capture_output=True, text=True)
    print('$', ' '.join(cmd), '->', r.returncode)
    print(r.stdout[-1500:])
    if r.stderr: print('STDERR:', r.stderr[-400:])
# check tail of file for sibling additions
p = 'query-cosientist.md'
lines = open(p).read().splitlines()
print('TOTAL', len(lines))
print('=== TAIL 15 ===')
for l in lines[-15:]:
    print(l[:250])
out.close()
