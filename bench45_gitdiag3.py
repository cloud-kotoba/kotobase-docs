import subprocess, io
cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
def run(args):
    r = subprocess.run(args, capture_output=True, text=True, cwd=cwd)
    return "RC=%d\nSTDOUT:\n%s\nSTDERR:\n%s" % (r.returncode, r.stdout, r.stderr)

out = []
out.append("== git log HEAD..upstream ==")
out.append(run(["git", "log", "--oneline", "HEAD..@{upstream}"]))
out.append("== rev-parse HEAD ==")
out.append(run(["git", "rev-parse", "HEAD"]))
out.append("== rev-parse upstream ==")
out.append(run(["git", "rev-parse", "@{upstream}"]))
out.append("== reflog -5 ==")
out.append(run(["git", "reflog", "-5"]))
io.open(cwd + "/bench45_gitdiag3.txt", "w").write("\n".join(out) + "\n")
print("done")
