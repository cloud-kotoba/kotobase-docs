import subprocess
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"

def run(args):
    p = subprocess.run(["git", "-C", repo] + args, capture_output=True, text=True, timeout=120)
    return (p.returncode, p.stdout.strip(), p.stderr.strip())

rc, out, err = run(["checkout", "net-kotobase/main"])
print("CHECKOUT rc=", rc)
print(out)
print(err)
rc, out, err = run(["log", "HEAD", "--oneline", "-3"])
print(out or err)
