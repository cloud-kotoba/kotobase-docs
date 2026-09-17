import subprocess, json

DOC = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
out = []

def run(cmd):
    r = subprocess.run(cmd, capture_output=True, text=True)
    out.append("$ %s\n%s%s(rc=%s)\n" % (" ".join(cmd), r.stdout, r.stderr, r.returncode))

# git state
run(["git", "rev-parse", "--abbrev-ref", "HEAD"])
run(["git", "log", "--oneline", "-2"])
run(["git", "pull", "--ff-only"])
run(["git", "log", "--oneline", "-2"])

# host load
run(["/usr/bin/uptime"])

# K-Z2 hypothesis row (grep in hypothesis population section)
r = subprocess.run(["/usr/bin/grep", "-n", "K-Z2", DOC], capture_output=True, text=True)
lines = r.stdout.strip().split("\n")
out.append("K-Z2 lines: %d\n" % len(lines))
# print first 6 occurrences (hypothesis rows are early)
for ln in lines[:8]:
    out.append(ln + "\n")

with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench36_diag_out.txt", "w") as f:
    f.writelines(out)
