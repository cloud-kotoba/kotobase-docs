import subprocess, os
repo = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
out = open('/tmp/fz_git.txt', 'w')
def run(cmd):
    r = subprocess.run(cmd, shell=True, cwd=repo, capture_output=True, text=True)
    out.write(f'$ {cmd}\n{r.stdout}{r.stderr}\n')
run('git add query-cosientist.md kq1_backend_stage2.mjs fz_append.py')
run('git commit -m "falsify 第39回: K-Q1 backend query path 計測第2段 (K-Q2 harness 再使用 + TTFB/total 分解: authenticated warm query p50 656.70/654.61ms, TTFB≈total — gateway auth check p50 20.11/21.31ms との差分 ~635ms が backend 実行区間に帰属, 2 run 再現) + Iteration log"')
run('git push net-kotobase HEAD:main')
out.close()
