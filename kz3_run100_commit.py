import subprocess

repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
msg = ("falsify: K-Z3 midnight 23h run100A-C evidence (100A cold 2/20 scattered "
       "1.073/2.062s, 100B-C cold 0/20, control clean, separate from cosientist run99)")

r = subprocess.run(["git", "-C", repo, "add", "query-cosientist.md"],
                   capture_output=True, text=True)
print("add:", r.returncode, r.stdout[-200:], r.stderr[-200:])
r = subprocess.run(["git", "-C", repo, "commit", "-m", msg],
                   capture_output=True, text=True)
print("commit:", r.returncode, r.stdout[-300:], r.stderr[-300:])
r = subprocess.run(["git", "-C", repo, "push", "net-kotobase", "HEAD:main"],
                   capture_output=True, text=True)
print("push:", r.returncode, r.stdout[-300:], r.stderr[-300:])
