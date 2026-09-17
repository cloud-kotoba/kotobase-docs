import subprocess

def run(cmd, timeout=120):
    p = subprocess.run(cmd, shell=True, capture_output=True, text=True, timeout=timeout, cwd='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
    return (p.stdout + p.stderr).strip()

out = []
out.append(run("git add query-cosientist.md kz3_run114.sh kz3_run114_out.txt kz3_run114_calc.py kz3_run114_append.py kz3_run114_append_wrap.py kz3_run114_verify.py falsify113_state.py falsify113_state2.py falsify113_state3.py falsify113_state4.py falsify113_state5.py && git commit -m 'falsify: K-Z3 深夜 5時台 run114A-C evidence (cold 0/60 完全静穏, 深夜帯通算 92/29 ~31.5%)'"))
out.append(run("git push net-kotobase HEAD:main 2>&1 | tail -3"))
open('/tmp/fz_commit114.txt', 'w').write('\n'.join(out))
print('ok')
