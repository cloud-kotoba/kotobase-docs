import subprocess
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
p = subprocess.run(["git", "-C", repo, "diff", "--stat"], capture_output=True, text=True)
print("rc:", p.returncode)
print(p.stdout or p.stderr)
p2 = subprocess.run(["git", "-C", repo, "diff", "query-cosientist.md"], capture_output=True, text=True)
print(p2.stdout[:3000])
