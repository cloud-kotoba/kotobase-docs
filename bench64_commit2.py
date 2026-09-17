import subprocess

def run(args):
    r = subprocess.run(args, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()

with open("bench64_commit2_out.txt", "w") as f:
    rc, out = run(["git", "add", "query-cosientist.md"])
    f.write("add rc=%d %s\n" % (rc, out))
    rc, out = run(["git", "commit", "-m",
        "docs: bench 第64回 evidence — K-Z3 3時台 2 セット目 run181A-C (cold 1/60 単発, run180A 多発は即時非再現) + bench63 記録修復の iteration log"])
    f.write("commit rc=%d %s\n" % (rc, out))
    rc, out = run(["git", "push", "net-kotobase", "HEAD:main"])
    f.write("push rc=%d %s\n" % (rc, out))
    rc, out = run(["git", "log", "-1", "--oneline"])
    f.write("head %s\n" % out)
