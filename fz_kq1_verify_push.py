import subprocess
# verify remote state matches local push
r = subprocess.run(["git", "fetch", "net-kotobase"], capture_output=True, text=True)
print("fetch:", r.returncode)
r = subprocess.run(["git", "rev-parse", "HEAD"], capture_output=True, text=True)
local = r.stdout.strip()
r = subprocess.run(["git", "rev-parse", "net-kotobase/main"], capture_output=True, text=True)
remote = r.stdout.strip()
print("local :", local)
print("remote:", remote)
print("match :", local == remote)
