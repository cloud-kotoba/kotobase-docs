import subprocess, io
cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
def run(args):
    r = subprocess.run(args, capture_output=True, text=True, cwd=cwd)
    return "RC=%d\nSTDOUT:\n%s\nSTDERR:\n%s" % (r.returncode, r.stdout, r.stderr)

out = []
out.append("== branches ==")
out.append(run(["git", "branch", "-a"]))
out.append("== net-kotobase/main vs HEAD ==")
out.append(run(["git", "log", "--oneline", "HEAD..net-kotobase/main"]))
out.append("== net-kotobase/main log -2 ==")
out.append(run(["git", "log", "--oneline", "-2", "net-kotobase/main"]))
io.open(cwd + "/bench45_gitdiag4.txt", "w").write("\n".join(out) + "\n")
print("done")
