import subprocess
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"

def run(args):
    p = subprocess.run(["git", "-C", repo] + args, capture_output=True, text=True, timeout=120)
    return (p.returncode, p.stdout.strip(), p.stderr.strip())

for label, args in [
    ("FETCH", ["fetch", "origin"]),
    ("HEAD", ["rev-parse", "HEAD"]),
    ("ORIGIN_MAIN", ["rev-parse", "origin/main"]),
    ("BRANCH", ["branch", "--show-current"]),
    ("REMOTE", ["remote", "-v"]),
    ("LOG_ORIGIN", ["log", "origin/main", "--oneline", "-5"]),
]:
    rc, out, err = run(args)
    print(f"== {label} rc={rc}")
    if out:
        print(out)
    if err:
        print("STDERR:", err)
