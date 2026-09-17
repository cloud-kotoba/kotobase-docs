import subprocess
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine"
r = subprocess.run(["npx", "wrangler", "deployments", "list"], cwd=repo, capture_output=True, text=True, timeout=120)
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/cos_iter51_deploy_full.txt", "w").write("RC=%d\n" % r.returncode + r.stdout + "\n---STDERR---\n" + r.stderr[-500:])
print("rc", r.returncode)
