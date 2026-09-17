import subprocess
cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
out = []
# 1) confirm pushed commit is on remote
r = subprocess.run(["git", "log", "--oneline", "origin/main", "-1"], capture_output=True, text=True, cwd=cwd)
out.append("origin/main tip: " + r.stdout.strip() + r.stderr.strip())
r = subprocess.run(["git", "log", "--oneline", "-2"], capture_output=True, text=True, cwd=cwd)
out.append("local log:\n" + r.stdout.strip())
# 2) verify K-Z3 row tail (evidence appended, no secrets)
r = subprocess.run(["/usr/bin/grep", "-c", "run107", "query-cosientist.md"], capture_output=True, text=True, cwd=cwd)
out.append("run107 occurrences: " + r.stdout.strip())
with open("bench37_verify2.txt", "w") as f:
    f.write("\n".join(out) + "\n")
