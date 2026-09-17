import subprocess
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"

def run(args):
    p = subprocess.run(["git", "-C", repo] + args, capture_output=True, text=True, timeout=120)
    return (p.returncode, p.stdout.strip(), p.stderr.strip())

rc, out, err = run(["fetch", "net-kotobase"])
print(f"FETCH rc={rc}")
print(out)
print(err)
for label, args in [
    ("LOG_REMOTE_MAIN", ["log", "net-kotobase/main", "--oneline", "-5"]),
    ("LOCAL_HEAD", ["log", "HEAD", "--oneline", "-3"]),
]:
    rc, out, err = run(args)
    print(f"== {label} rc={rc}")
    print(out or err)
