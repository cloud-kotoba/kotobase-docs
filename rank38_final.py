import sys, os
out = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rank38_out16.txt','w')
sys.stdout = out
import subprocess
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
def run(*cmd):
    r = subprocess.run(list(cmd), capture_output=True, text=True)
    print('$', ' '.join(cmd), '->', r.returncode)
    print(r.stdout[-1500:])
    if r.stderr: print('STDERR:', r.stderr[-500:])
# 報告用に最終状態確認のみ (branch 切替は fleet 共有 worktree のため他 bot と衝突する恐れがあり実施しない)
run('git','rev-parse','HEAD')
run('git','log','--oneline','-1')
out.close()
