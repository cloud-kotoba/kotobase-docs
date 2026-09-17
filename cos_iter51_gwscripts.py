import subprocess
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/control-plane/kotobase-api-gateway-cljs"
env = {"PATH": "/usr/bin:/bin:/usr/local/bin:/opt/homebrew/bin", "HOME": "/Users/junkawasaki", "CI": "1"}
r = subprocess.run(["npm", "run"], cwd=repo, capture_output=True, text=True, timeout=60, env=env)
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/cos_iter51_gwscripts.txt", "w").write(r.stdout + r.stderr)
print("rc", r.returncode)
