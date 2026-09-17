import subprocess

def run(args):
    r = subprocess.run(args, capture_output=True, text=True,
                       cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
    return (r.returncode, r.stdout.strip(), r.stderr.strip())

rc, out, err = run(["git", "log", "--oneline", "-3"])
print("log", rc, out, err)
rc, out, err = run(["git", "push", "net-kotobase", "main"])
print("push", rc, out, err)
rc, out, err = run(["git", "rev-parse", "net-kotobase/main"])
print("remote_after_fetch_may_be_stale", rc, out, err)
