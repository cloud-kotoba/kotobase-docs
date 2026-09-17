import subprocess

def run(*args):
    r = subprocess.run(args, capture_output=True, text=True, cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs", timeout=180)
    return r.returncode, (r.stdout + r.stderr).strip()

rc, out = run("git", "push", "net-kotobase", "HEAD:refs/heads/main")
with open("/tmp/bench65_push2.txt", "w") as f:
    f.write(f"push rc={rc}\n{out}\n")
print("rc", rc)
