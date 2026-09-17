import subprocess, io
def run(args, cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True)
    return r.returncode, (r.stdout + r.stderr).strip()
out = []
# Where did run174 land in main? Check whether it's in the K-Z3 hypothesis row or only iteration log.
rc, o = run(["git", "show", "net-kotobase/main:query-cosientist.md"])
main = o
out.append(("main run174 count", 0, str(main.count("run174"))))
# find K-Z3 row line in main
kz3 = [ln for ln in main.split("\n") if ln.startswith("| K-Z3 | worker |")]
out.append(("kz3 rows in main", 0, str(len(kz3))))
out.append(("run174A in kz3 row", 0, str(any("run174A" in ln for ln in kz3))))
# which commit contains run174?
rc, o = run(["git", "log", "--oneline", "-3", "net-kotobase/main"])
out.append(("main log", rc, o))
rc, o = run(["git", "log", "--oneline", "-S", "run174A", "net-kotobase/main", "--", "query-cosientist.md"])
out.append(("run174 commit", rc, o))
io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench60_gitdiag5.txt", "w", encoding="utf-8").write("\n".join(str(x) for x in out))
