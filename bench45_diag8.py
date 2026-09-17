import subprocess, io
cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
def run(args):
    r = subprocess.run(args, capture_output=True, text=True, cwd=cwd)
    return "RC=%d\n%s%s" % (r.returncode, r.stdout, r.stderr)

out = []
out.append("== reflog -8 ==")
out.append(run(["git", "reflog", "-8"]))
out.append("== remote net-kotobase/main latest ==")
out.append(run(["git", "log", "--oneline", "-1", "net-kotobase/main"]))
out.append("== show remote blob run125 count ==")
r = subprocess.run(["git", "grep", "-c", "run125", "net-kotobase/main", "--", "query-cosientist.md"],
                   capture_output=True, text=True, cwd=cwd)
out.append("RC=%d out=%r err=%r" % (r.returncode, r.stdout, r.stderr))
out.append("== show remote blob iteration log tail ==")
blob = subprocess.run(["git", "show", "net-kotobase/main:query-cosientist.md"], capture_output=True, text=True, cwd=cwd).stdout
out.append("remote blob has 'bench 第45回': %s" % ("bench 第45回" in blob))
out.append("remote blob has run125A: %d" % blob.count("run125A"))
open(cwd + "/bench45_diag8.txt", "w").write("\n".join(out)[:10000])
print("done")
