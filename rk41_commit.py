import subprocess
r = subprocess.run(['git', 'add', 'query-cosientist.md'], capture_output=True, text=True)
print(r.returncode, r.stdout, r.stderr)
r = subprocess.run(['git', 'commit', '-m',
  'rank 第41回: K-Z3 run116-119 採用 (6時台 15試行中2試行 ~13%, 8時台帯初計測 cold 0/60, 深夜帯通算 107試行中30試行 ~28%), status 遷移なし, NEXT: K-Z3 9時台 n 積み増し'],
  capture_output=True, text=True)
print(r.returncode, r.stdout, r.stderr)
