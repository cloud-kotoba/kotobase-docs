import subprocess
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine"
r = subprocess.run(["node", "scripts/deploy-versioned.mjs", "production", "--confirm-production", "7dc62497d0ffe6c492c3b3b5510f1c12ad5a9fe9"],
                   cwd=repo, capture_output=True, text=True, timeout=540)
out = "RC=%d\n" % r.returncode + r.stdout[-5000:] + "\n---STDERR---\n" + r.stderr[-2000:]
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/cos_iter51_deploy_run.txt", "w").write(out)
print("deploy rc", r.returncode)
