import subprocess, io
def run(args, cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()
out = []
# check whether run174 evidence exists in the checked-out HEAD version of the file
rc, o = run(["git", "show", "HEAD:query-cosientist.md"])
has_head = "run174" in o
out.append(("HEAD has run174", rc, has_head))
# grep for run174 in remote main version
rc, o = run(["git", "show", "net-kotobase/main:query-cosientist.md"])
has_main = "run174" in o
out.append(("main has run174", rc, has_main))
# our commit didn't get created (commit rc=1) because HEAD detached? Actually commit failed with rc 1 —
# output showed untracked files listing => "nothing added to commit"? We did git add first though.
# Check stash/index: is there staged content?
rc, o = run(["git", "stash", "list"])
out.append(("stash", rc, o))
rc, o = run(["git", "diff", "HEAD", "--stat"])
out.append(("worktree vs HEAD", rc, o[:200]))
io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench60_gitdiag4.txt", "w", encoding="utf-8").write("\n".join(str(x) for x in out))
