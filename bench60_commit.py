import subprocess, io

def run(args, cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()

out = []
rc, o = run(["git", "add", "query-cosientist.md"])
out.append(("add", rc, o))
msg = "bench: 第60回 K-Z3 22時台 n 積み増し run174A-C (1/60, control 静穏, 22時台通算 7/180 ~3.9%)"
rc, o = run(["git", "commit", "-m", msg, "query-cosientist.md"])
out.append(("commit", rc, o[:600]))
rc, o = run(["git", "pull", "--rebase", "origin", "main"])
out.append(("pull-rebase", rc, o[:400]))
rc, o = run(["git", "push", "origin", "HEAD:main"])
out.append(("push", rc, o[:400]))
io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench60_commit_out.txt", "w", encoding="utf-8").write("\n".join(str(x) for x in out))
print("done")
