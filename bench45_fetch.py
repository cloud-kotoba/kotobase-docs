import subprocess, io, time
cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
def run(args):
    r = subprocess.run(args, capture_output=True, text=True, cwd=cwd)
    return "RC=%d\nSTDOUT:\n%s\nSTDERR:\n%s" % (r.returncode, r.stdout, r.stderr)

out = []
out.append("== fetch ==")
out.append(run(["git", "fetch", "net-kotobase"]))
out.append("== log HEAD..net-kotobase/main after fetch ==")
out.append(run(["git", "log", "--oneline", "HEAD..net-kotobase/main"]))
io.open(cwd + "/bench45_fetch.txt", "w").write("\n".join(out) + "\n")
print("done")
