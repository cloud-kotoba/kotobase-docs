import subprocess, io
cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
def run(args):
    r = subprocess.run(args, capture_output=True, text=True, cwd=cwd)
    return "RC=%d\n%s%s" % (r.returncode, r.stdout, r.stderr)

out = []
out.append("== does HEAD file contain run125? ==")
blob = subprocess.run(["git", "show", "HEAD:query-cosientist.md"], capture_output=True, text=True, cwd=cwd).stdout
out.append("HEAD blob run125 count: %d" % blob.count("run125A"))
wt = io.open(cwd + "/query-cosientist.md", encoding="utf-8").read()
out.append("worktree run125 count: %d" % wt.count("run125A"))
out.append("identical bytes: %s" % (blob == wt))
out.append("== git stash list ==")
out.append(run(["git", "stash", "list"]))
out.append("== git ls-files -m ==")
out.append(run(["git", "ls-files", "-m"]))
out.append("== git fsck quick ==")
out.append(run(["git", "status"]))
io.open(cwd + "/bench45_diag5.txt", "w").write("\n".join(out)[:12000])
print("done")
