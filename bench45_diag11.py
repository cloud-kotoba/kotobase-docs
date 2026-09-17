import subprocess, io
cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
r2 = subprocess.run(["git", "show", "eee3314", "--", "query-cosientist.md"], capture_output=True, text=True, cwd=cwd)
lines = r2.stdout.split("\n")
# print the iteration-log entry hunk around line 60 hit
for i in range(55, 75):
    print("L%d: %s" % (i, lines[i][:300]))
