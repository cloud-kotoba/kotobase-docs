import subprocess, io
cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
# The K-Z3 hypothesis row in the worktree: check if the row evidence appended by us
# landed in HEAD (search K-Z3 row for our exact addition)
blob = subprocess.run(["git", "show", "HEAD:query-cosientist.md"], capture_output=True, text=True, cwd=cwd).stdout
rows = [ln for ln in blob.split("\n") if ln.startswith("| K-Z3 | worker |")]
with io.open(cwd + "/bench45_diag12.txt", "w", encoding="utf-8") as f:
    f.write("K-Z3 rows in HEAD: %d\n" % len(rows))
    for ln in rows:
        f.write("has 10時台帯初計測 run125A–C: %s\n" % ("10時台帯初計測 run125A–C" in ln))
        f.write("row tail 300: ...%s\n" % ln[-300:])
print("done")
