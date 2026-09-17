import sys
out = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rank38_out9.txt','w')
sys.stdout = out
import subprocess, os
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
# HEAD moved? worktree clean but sizes differ -> HEAD must have moved
r = subprocess.run(['git','log','--oneline','-3'], capture_output=True, text=True)
print(r.stdout)
r = subprocess.run(['git','rev-parse','HEAD'], capture_output=True, text=True)
print('HEAD now:', r.stdout.strip())
r = subprocess.run(['git','diff','HEAD','--stat'], capture_output=True, text=True)
print('diff vs HEAD:', r.stdout[:2000])
out.close()
