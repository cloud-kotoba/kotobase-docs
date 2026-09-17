import sys
out = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rank38_out8.txt','w')
sys.stdout = out
import subprocess, os
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
r = subprocess.run(['git','show','--stat','HEAD'], capture_output=True, text=True)
print(r.stdout[-2000:])
r = subprocess.run(['git','show','HEAD','--stat','--format=%H %s'], capture_output=True, text=True)
print(r.stdout[-1500:])
# worktree file vs HEAD
r = subprocess.run(['git','show','HEAD:query-cosientist.md'], capture_output=True, text=True)
print('HEAD file size:', len(r.stdout))
print('worktree size:', os.path.getsize('query-cosientist.md'))
out.close()
