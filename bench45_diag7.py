import subprocess, io, os
cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
# Compare worktree file against HEAD blob byte-by-byte to confirm truly identical
blob = subprocess.run(["git", "show", "HEAD:query-cosientist.md"], capture_output=True, cwd=cwd).stdout
wt = open(cwd + "/query-cosientist.md", "rb").read()
out = []
out.append("HEAD blob bytes: %d" % len(blob))
out.append("worktree bytes: %d" % len(wt))
out.append("identical: %s" % (blob == wt))
# Check index entry
r = subprocess.run(["git", "ls-files", "-s", "query-cosientist.md"], capture_output=True, text=True, cwd=cwd)
out.append("index entry: %s" % r.stdout.strip())
r2 = subprocess.run(["git", "hash-object", "query-cosientist.md"], capture_output=True, text=True, cwd=cwd)
out.append("worktree hash: %s" % r2.stdout.strip())
r3 = subprocess.run(["git", "rev-parse", "HEAD:query-cosientist.md"], capture_output=True, text=True, cwd=cwd)
out.append("HEAD blob hash: %s" % r3.stdout.strip())
open(cwd + "/bench45_diag7.txt", "w").write("\n".join(out) + "\n")
print("done")
