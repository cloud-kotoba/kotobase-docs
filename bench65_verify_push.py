import subprocess
def run(*args):
    r = subprocess.run(args, capture_output=True, text=True, cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs", timeout=180)
    return r.returncode, (r.stdout + r.stderr).strip()
rc, out = run("git", "fetch", "net-kotobase")
rc2, out2 = run("git", "rev-parse", "net-kotobase/main")
rc3, out3 = run("git", "merge-base", "--is-ancestor", "HEAD", "net-kotobase/main")
print("fetch rc", rc, "main", out2, "ancestor_rc", rc3)
