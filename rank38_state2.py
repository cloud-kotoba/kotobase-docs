import sys, os
out = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rank38_out13.txt','w')
sys.stdout = out
import subprocess
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
print('exists:', os.path.exists('query-cosientist.md'))
print('size:', os.path.getsize('query-cosientist.md') if os.path.exists('query-cosientist.md') else 'N/A')
for cmd in [['git','status','--short'], ['git','rev-parse','HEAD'], ['git','diff','--stat']]:
    r = subprocess.run(cmd, capture_output=True, text=True)
    print('$', ' '.join(cmd), '->', r.returncode)
    print(r.stdout[:800])
    if r.stderr: print('ERR:', r.stderr[:300])
out.close()
