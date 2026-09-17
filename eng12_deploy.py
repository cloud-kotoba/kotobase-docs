import subprocess
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine"
r = subprocess.run(["node", "scripts/deploy-versioned.mjs", "production", "--confirm-production", "415b1b28ff1c64ae3ef7a34c6f7c1738b830cc11"],
                   cwd=repo, capture_output=True, text=True, timeout=540)
out = "RC=%d\n" % r.returncode + r.stdout[-4000:] + r.stderr[-2000:]
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/eng12_deploy.txt", "w").write(out)
print("deploy rc", r.returncode)
