import subprocess
r = subprocess.run(["git", "push", "origin", "HEAD:refs/heads/main"], cwd=".", capture_output=True, text=True)
print("PUSH RC", r.returncode)
print(r.stdout, r.stderr)
