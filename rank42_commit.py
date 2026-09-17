import subprocess

msg = ('rank 第42回: K-Z3 run121A-C 採用 (8時台 3 セット連続 cold 0/180 完全静穏, '
       '深夜帯通算 116 試行中 30 試行 ~25.9%), status 遷移なし, '
       'NEXT: K-Z3 9時台 n 積み増し')
subprocess.run(['git', 'add', 'query-cosientist.md'], check=True)
subprocess.run(['git', 'commit', '-m', msg], check=True)
subprocess.run(['git', 'push', 'net-kotobase', 'HEAD:main'], check=True)
r = subprocess.run(['git', 'log', '--oneline', '-2'], capture_output=True, text=True)
print(r.stdout)
