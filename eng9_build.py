import subprocess
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine"
r = subprocess.run(["npx", "shadow-cljs", "release", "worker"], cwd=repo, capture_output=True, text=True, timeout=540)
out = "RC=%d\n" % r.returncode + r.stdout[-3000:] + r.stderr[-3000:]
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/eng9_build.txt", "w").write(out)
print("build rc", r.returncode)
