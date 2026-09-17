import subprocess, io
def run(args, cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()
out = []
# remote is named net-kotobase (not origin); remote URL lacks .git suffix. Test fetch.
rc, o = run(["git", "fetch", "net-kotobase", "main"])
out.append(("fetch", rc, o[:300]))
# rebase local state (detached HEAD with our commit on top of 8f1b9c3) onto latest main
rc, o = run(["git", "log", "--oneline", "-2"])
out.append(("log-pre", rc, o))
# our local commit: check status after fetch
rc, o = run(["git", "status", "-sb"])
out.append(("status", rc, o.split("\n")[0]))
io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench60_gitdiag2.txt", "w", encoding="utf-8").write("\n".join(str(x) for x in out))
