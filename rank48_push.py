import subprocess

cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
lines = []
def run(*cmd):
    p = subprocess.run(list(cmd), cwd=cwd, capture_output=True, text=True)
    lines.append("$ " + " ".join(cmd))
    lines.append(p.stdout.strip())
    if p.stderr.strip():
        lines.append("STDERR: " + p.stderr.strip())
    lines.append("RC=%d" % p.returncode)
    lines.append("")
    return p

# ensure remote main hasn't moved ahead of our commit
run("git", "fetch", "net-kotobase")
run("git", "log", "--oneline", "-1", "net-kotobase/main")
p = subprocess.run(["git", "merge-base", "--is-ancestor", "net-kotobase/main", "HEAD"],
                   cwd=cwd, capture_output=True, text=True)
lines.append("merge-base --is-ancestor main HEAD RC=%d (0 = our HEAD contains remote main)" % p.returncode)
lines.append("")
if p.returncode == 0:
    run("git", "push", "net-kotobase", "HEAD:main")
else:
    lines.append("ABORT: remote main is ahead; not pushing.")
run("git", "log", "--oneline", "-2", "net-kotobase/main")
with open(cwd + "/rank48_push_out.txt", "w") as f:
    f.write("\n".join(lines))
