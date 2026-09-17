import subprocess
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/control-plane/kotobase-api-gateway-cljs"
env = {"PATH": "/usr/bin:/bin:/usr/local/bin:/opt/homebrew/bin", "HOME": "/Users/junkawasaki", "CI": "1"}
r = subprocess.run(["npm", "test"], cwd=repo, capture_output=True, text=True, timeout=560, env=env)
out = "RC=%d\n" % r.returncode + r.stdout[-4000:] + "\n---STDERR---\n" + r.stderr[-1500:]
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/cos_iter51_gwtest2.txt", "w").write(out)
print("test rc", r.returncode)
