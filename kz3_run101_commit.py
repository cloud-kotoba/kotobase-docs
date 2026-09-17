import subprocess

cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
msg = ("bench: K-Z3 midnight 23h run101A-C evidence (101A cold 3/20 scattered 1.08-1.52s, "
       "101B-C cold 0/20, control clean, 3rd consecutive midnight cold-cluster like run99A/100A)")
r = subprocess.run(["git", "add", "query-cosientist.md"], capture_output=True, text=True, cwd=cwd)
print(r.returncode, r.stderr)
r = subprocess.run(["git", "commit", "-m", msg], capture_output=True, text=True, cwd=cwd)
print(r.returncode, r.stdout[-500:], r.stderr[-500:])
r = subprocess.run(["git", "push", "net-kotobase", "HEAD:main"], capture_output=True, text=True, cwd=cwd)
print(r.returncode, r.stdout[-500:], r.stderr[-500:])
