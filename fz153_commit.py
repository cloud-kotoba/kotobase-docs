import subprocess
msg = """falsify 第52回: K-Z3 14時台 n 積み増し run153A-C (cold 0/60 完全静穏, control 静穏 — 14時台初計測) + landing control 同時刻 n=20 静穏"""
r = subprocess.run(['git', 'add', 'query-cosientist.md'], capture_output=True, text=True)
print(r.stdout, r.stderr)
r = subprocess.run(['git', 'commit', '-m', msg], capture_output=True, text=True)
print(r.stdout, r.stderr)
r = subprocess.run(['git', 'push', 'net-kotobase', 'HEAD:main'], capture_output=True, text=True)
print(r.stdout, r.stderr)
