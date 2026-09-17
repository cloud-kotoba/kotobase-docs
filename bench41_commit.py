import subprocess
msg = ("bench 第41回: K-Z3 6時台 n 積み増し run117A-C (cold 0/60 完全静穏, control 静穏 — "
       "6時台通算 12 試行中 2 試行 ~17%, 深夜帯通算 101 試行中 30 試行 ~29.7%)")
r = subprocess.run(["git", "add", "query-cosientist.md"], cwd=".", capture_output=True, text=True)
print(r.stdout, r.stderr)
r = subprocess.run(["git", "commit", "-m", msg], cwd=".", capture_output=True, text=True)
print(r.stdout, r.stderr)
r = subprocess.run(["git", "push", "HEAD:refs/heads/main"], cwd=".", capture_output=True, text=True)
print("PUSH RC", r.returncode)
print(r.stdout, r.stderr)
