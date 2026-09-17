import subprocess
subprocess.run(['git', 'add', 'query-cosientist.md', 'kz3_run154.sh', 'kz3_run154_out.txt',
                'kz3_run154_calc.py', 'kz3_run154_calc.txt', 'fz154_append.py',
                'fz154_append_out.txt', 'fz154_diff.txt'], check=True)
msg = ('falsify 第53回: K-Z3 16時台 n 積み増し run154A-C '
       '(cold 6/3/0 per 20, search のみ 1s 超外れ値 9/60, control 静穏 p50 59ms) '
       'evidence 追記 — status 遷移なし')
r = subprocess.run(['git', 'commit', '-m', msg], capture_output=True, text=True)
print(r.stdout, r.stderr)
r = subprocess.run(['git', 'push', 'net-kotobase', 'HEAD:main'], capture_output=True, text=True)
print(r.stdout, r.stderr)
