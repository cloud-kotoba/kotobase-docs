import subprocess, io
cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
# Check eee3314's actual diff to understand what it contains regarding run125
r = subprocess.run(["git", "show", "--stat", "eee3314"], capture_output=True, text=True, cwd=cwd)
r2 = subprocess.run(["git", "show", "eee3314", "--", "query-cosientist.md"], capture_output=True, text=True, cwd=cwd)
diff = r2.stdout
out = []
out.append(r.stdout)
out.append("DIFF LEN: %d" % len(diff))
# find hunks mentioning run125
lines = diff.split("\n")
for i, ln in enumerate(lines):
    if "run125" in ln:
        out.append("hunk line %d: %s" % (i, ln[:500]))
open(cwd + "/bench45_diag10.txt", "w").write("\n".join(out)[:15000])
print("done")
