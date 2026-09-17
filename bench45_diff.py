import subprocess
r = subprocess.run(["git", "diff", "query-cosientist.md"], capture_output=True, text=True,
                   cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench45_diff.txt", "w") as f:
    f.write(r.stdout + r.stderr)
print("done")
