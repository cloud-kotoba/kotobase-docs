import subprocess
cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
out = []
r = subprocess.run(["git", "remote", "-v"], capture_output=True, text=True, cwd=cwd)
out.append("remotes:\n" + r.stdout.strip())
r = subprocess.run(["git", "branch", "-a"], capture_output=True, text=True, cwd=cwd)
out.append("branches:\n" + r.stdout.strip())
r = subprocess.run(["git", "push"], capture_output=True, text=True, cwd=cwd)
out.append("push: rc=%d\n%s%s" % (r.returncode, r.stdout, r.stderr))
with open("bench37_verify3.txt", "w") as f:
    f.write("\n".join(out) + "\n")
