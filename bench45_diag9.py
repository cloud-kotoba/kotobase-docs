import subprocess, io
cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
def run(args):
    r = subprocess.run(args, capture_output=True, text=True, cwd=cwd)
    return "RC=%d\n%s%s" % (r.returncode, r.stdout, r.stderr)

# Find the commit that introduced run125
out = []
out.append(run(["git", "log", "--oneline", "-5", "-S", "run125", "--", "query-cosientist.md"]))
out.append("== full log -5 ==")
out.append(run(["git", "log", "--oneline", "-5"]))
open(cwd + "/bench45_diag9.txt", "w").write("\n".join(out)[:6000])
print("done")
