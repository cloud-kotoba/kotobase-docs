import subprocess
d = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
r = subprocess.run(["git", "fetch", "net-kotobase"], cwd=d, capture_output=True, text=True)
r2 = subprocess.run(["git", "rev-parse", "HEAD", "net-kotobase/main"], cwd=d, capture_output=True, text=True)
print("fetch rc", r.returncode)
print("HEAD == net-kotobase/main:", r2.stdout.split())
