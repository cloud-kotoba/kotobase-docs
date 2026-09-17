import subprocess, io
cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
# Search worktree blob for run125 to see if K-Z3 row AND iteration log present in HEAD blob
r = subprocess.run(["git", "show", "HEAD:query-cosientist.md"], capture_output=True, text=True, cwd=cwd)
blob = r.stdout
lines = blob.split("\n")
hits = [(i, ln) for i, ln in enumerate(lines, 1) if "run125" in ln]
with io.open(cwd + "/bench45_diag6.txt", "w", encoding="utf-8") as f:
    f.write("HEAD blob lines with run125: %d\n" % len(hits))
    for i, ln in hits[:10]:
        f.write("L%d: %s\n" % (i, ln[:400]))
print("done", len(hits))
