import subprocess
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"

def run(args):
    p = subprocess.run(["git", "-C", repo] + args, capture_output=True, text=True, timeout=120)
    return (p.returncode, p.stdout.strip(), p.stderr.strip())

rc, out, err = run(["branch", "-a"])
print("BRANCHES rc=", rc)
print(out or err)
rc, out, err = run(["merge-base", "HEAD", "net-kotobase/main"])
print("MERGE_BASE:", out or err)
