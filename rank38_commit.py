import sys, os
out = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rank38_out15.txt','w')
sys.stdout = out
import subprocess
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
def run(*cmd):
    r = subprocess.run(list(cmd), capture_output=True, text=True)
    print('$', ' '.join(cmd), '->', r.returncode)
    print(r.stdout[-3000:])
    if r.stderr: print('STDERR:', r.stderr[-800:])
    return r

run('git','add','query-cosientist.md')
r = run('git','commit','-m',
    'rank 第37回: K-Z2 対比 4 源累計 (run106 2/4 窓同方向, run107 直後 0 + 逆方向寄り) の方向非一貫確定, K-Z3 深夜帯 3時台 run107 を反映 (通算 28/85 ~32.9%, traffic 依存説反証材料増加), rank ブロック第37回版へ差替え, NEXT: K-Z2 対比 n 増強継続 (quiet-host tick は K-Q1 backend 計測優先)')
run('git','push','net-kotobase','HEAD:main')
r = run('git','fetch','net-kotobase')
r = run('git','log','--oneline','-2','net-kotobase/main')
out.close()
