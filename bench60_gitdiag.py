import subprocess, io
def run(args):
    r = subprocess.run(args, cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs", capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()
out = []
for cmd in [["git", "remote", "-v"], ["git", "status", "-sb"], ["git", "log", "--oneline", "-3"], ["git", "branch", "-a"]]:
    rc, o = run(cmd)
    out.append((cmd, rc, o[:500]))
io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench60_gitdiag.txt", "w", encoding="utf-8").write("\n".join(str(x) for x in out))
