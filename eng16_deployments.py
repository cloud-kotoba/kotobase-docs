import subprocess
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine"
r = subprocess.run(["npx", "wrangler", "deployments", "list"], cwd=repo, capture_output=True, text=True, timeout=120)
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/eng16_deployments.txt", "w").write("RC=%d\n" % r.returncode + r.stdout[:3000] + r.stderr[:800])
print("rc", r.returncode)
