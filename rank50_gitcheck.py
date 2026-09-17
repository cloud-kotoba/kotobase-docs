#!/usr/bin/env python3
import subprocess
cmds = [
    ["git", "show", "--stat", "--oneline", "4fa6a0c"],
    ["git", "log", "--oneline", "-3", "--all", "--source"],
    ["git", "status", "-sb"],
]
out = []
for c in cmds:
    r = subprocess.run(c, capture_output=True, text=True,
                       cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
    out.append("$ " + " ".join(c) + "\n" + (r.stdout + r.stderr)[:2000] + "\n")
open("/tmp/rank50_git2.txt", "w").write("\n".join(out))
print("done")
