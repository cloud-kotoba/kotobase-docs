import subprocess, io
def run(args, cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()
out = []
# how far ahead is remote main vs our base?
rc, o = run(["git", "rev-list", "--count", "HEAD..net-kotobase/main"])
out.append(("behind-count", rc, o))
rc, o = run(["git", "rev-list", "--count", "net-kotobase/main..HEAD"])
out.append(("ahead-count", rc, o))
# Is our working tree change committed? We did git add + commit failed, so check
rc, o = run(["git", "diff", "--stat", "HEAD", "--", "query-cosientist.md"])
out.append(("diff-stat", rc, o))
rc, o = run(["git", "diff", "--cached", "--stat"])
out.append(("cached-stat", rc, o))
io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench60_gitdiag3.txt", "w", encoding="utf-8").write("\n".join(str(x) for x in out))
