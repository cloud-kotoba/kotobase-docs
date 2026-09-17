import subprocess, io
cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"

# The worktree file has the edits; HEAD does not. Check explicitly.
r = subprocess.run(["git", "status", "--porcelain", "--", "query-cosientist.md"],
                   capture_output=True, text=True, cwd=cwd)
st = r.stdout
r2 = subprocess.run(["git", "diff", "--numstat", "--", "query-cosientist.md"],
                    capture_output=True, text=True, cwd=cwd)

src = io.open(cwd + "/query-cosientist.md", encoding="utf-8").read()
has_row = "run125A cold(>=0.5s) 1/20" in src
has_log = "bench 第45回" in src

out = []
out.append("porcelain: %r" % st)
out.append("numstat: %r" % r2.stdout)
out.append("worktree has K-Z3 row evidence: %s" % has_row)
out.append("worktree has iteration log entry: %s" % has_log)

# Re-run add + commit with author info check
r3 = subprocess.run(["git", "add", "query-cosientist.md"], capture_output=True, text=True, cwd=cwd)
out.append("add RC=%d %s%s" % (r3.returncode, r3.stdout, r3.stderr))
r4 = subprocess.run(["git", "status", "--porcelain", "--", "query-cosientist.md"],
                    capture_output=True, text=True, cwd=cwd)
out.append("porcelain after add: %r" % r4.stdout)

io.open(cwd + "/bench45_stagecheck.txt", "w").write("\n".join(out) + "\n")
print("done")
