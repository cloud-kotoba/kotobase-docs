import subprocess, io
cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
def run(args):
    r = subprocess.run(args, capture_output=True, text=True, cwd=cwd)
    return "RC=%d\n%s%s" % (r.returncode, r.stdout, r.stderr)

out = []
out.append("== git log -1 HEAD ==")
out.append(run(["git", "log", "--oneline", "-1"]))
out.append("== show HEAD:query-cosientist.md run125 ==")
out.append(run(["git", "show", "HEAD:query-cosientist.md"]))
out.append("== status of file ==")
out.append(run(["git", "status", "--short", "query-cosientist.md"]))
blob = run(["git", "grep", "-c", "run125A", "HEAD", "--", "query-cosientist.md"])
out.append("== grep HEAD for run125A ==\n" + blob)
txt = "\n".join(out)
io.open(cwd + "/bench45_remotecheck.txt", "w").write(txt[:8000])
print("run125A lines shown:", txt.count("run125A"))
