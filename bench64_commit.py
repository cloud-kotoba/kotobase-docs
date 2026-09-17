import subprocess

def run(args):
    r = subprocess.run(args, capture_output=True, text=True)
    out = (r.stdout + r.stderr).strip()
    return r.returncode, out

with open("bench64_commit_out.txt", "w") as f:
    rc, out = run(["git", "add", "query-cosientist.md"])
    f.write("add rc=%d %s\n" % (rc, out))
    rc, out = run(["git", "commit", "-m",
        "docs: bench 第63回 evidence — K-Q1 transact 401 再試行 (2回連続401, no fabricated data) + K-Z3 3時台 run180A-C (cold 9/0/1 per 20, control 静穏)"])
    f.write("commit rc=%d %s\n" % (rc, out))
    rc, out = run(["git", "push", "net-kotobase", "HEAD:main"])
    f.write("push rc=%d %s\n" % (rc, out))
    rc, out = run(["git", "log", "-1", "--oneline"])
    f.write("head %s\n" % out)
