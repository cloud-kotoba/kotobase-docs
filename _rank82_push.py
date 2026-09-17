import subprocess, json
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
r1 = subprocess.run(["git", "-C", p, "status", "--porcelain", "--", "query-cosientist.md"], capture_output=True, text=True)
r2 = subprocess.run(["git", "-C", p, "log", "--oneline", "-2"], capture_output=True, text=True)
r3 = subprocess.run(["git", "-C", p, "fetch", "net-kotobase"], capture_output=True, text=True)
r4 = subprocess.run(["git", "-C", p, "rev-parse", "HEAD", "net-kotobase/main"], capture_output=True, text=True)
r5 = subprocess.run(["git", "-C", p, "push", "net-kotobase", "HEAD:main"], capture_output=True, text=True)
with open("/tmp/rank82_push.txt", "w") as f:
    for name, r in [("status", r1), ("log", r2), ("fetch", r3), ("revparse", r4), ("push", r5)]:
        f.write(f"{name} rc={r.returncode}\nOUT {r.stdout[-600:]}\nERR {r.stderr[-600:]}\n\n")
