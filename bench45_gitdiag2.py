import subprocess, io
cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
def run(args):
    r = subprocess.run(args, capture_output=True, text=True, cwd=cwd)
    return r.stdout + r.stderr

out = []
out.append("== status ==")
out.append(run(["git", "status", "--short"]))
out.append("== branch ==")
out.append(run(["git", "rev-parse", "--abbrev-ref", "HEAD"]))
out.append("== last commit touching file ==")
out.append(run(["git", "log", "--oneline", "-1", "--", "query-cosientist.md"]))
out.append("== worktree file head of K-Z3 row check ==")
src = io.open(cwd + "/query-cosientist.md", encoding="utf-8").read()
out.append("run125A cold in file: %s" % ("run125A cold(>=0.5s) 1/20" in src))
out.append("bench 第45回 in file: %s" % ("bench 第45回" in src))
io.open(cwd + "/bench45_gitdiag2.txt", "w").write("\n".join(out) + "\n")
print("done")
