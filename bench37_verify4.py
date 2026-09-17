import subprocess
cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
r = subprocess.run(["git", "log", "--oneline", "net-kotobase/main", "-1"], capture_output=True, text=True, cwd=cwd)
with open("bench37_verify4.txt", "w") as f:
    f.write("remote tip: " + r.stdout.strip() + r.stderr.strip() + "\n")
