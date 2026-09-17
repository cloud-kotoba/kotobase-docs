import subprocess
r = subprocess.run(["git", "diff", "HEAD", "--", "query-cosientist.md"], capture_output=True, text=True,
                   cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench45_diff2.txt", "w") as f:
    f.write("STDERR: " + r.stderr + "\n")
    f.write(r.stdout[:6000])
print("done", len(r.stdout))
