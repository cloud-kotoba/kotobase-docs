import subprocess
r = subprocess.run(["git", "diff", "--stat"], capture_output=True, text=True,
                   cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
r2 = subprocess.run(["git", "status", "--short"], capture_output=True, text=True,
                    cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench45_verify.txt", "w") as f:
    f.write(r.stdout + r.stderr + "--\n" + r2.stdout + r2.stderr)
print("done")
