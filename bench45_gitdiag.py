import subprocess
def run(args):
    r = subprocess.run(args, capture_output=True, text=True,
                       cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
    return (r.returncode, r.stdout[:1500], r.stderr[:500])
out = []
out.append("status: %r" % (run(["git", "status", "--short", "query-cosientist.md"]),))
out.append("branch: %r" % (run(["git", "branch", "--show-current"]),))
out.append("log2: %r" % (run(["git", "log", "--oneline", "-2"]),))
with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench45_gitdiag.txt", "w") as f:
    f.write("\n".join(out) + "\n")
print("done")
