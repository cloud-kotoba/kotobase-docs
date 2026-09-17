import subprocess, io
cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
# Amend is risky; instead just verify push state. Remote net-kotobase/main == HEAD?
r = subprocess.run(["git", "rev-parse", "net-kotobase/main", "HEAD"], capture_output=True, text=True, cwd=cwd)
with io.open(cwd + "/bench45_diag13.txt", "w") as f:
    f.write(r.stdout + r.stderr)
print("done")
