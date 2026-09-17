import subprocess
out = []
for cmd in (["git", "log", "--oneline", "-5"],
            ["git", "status", "--porcelain", "query-cosientist.md"],
            ["git", "log", "-1", "--format=%H %ci %s"]):
    r = subprocess.run(cmd, capture_output=True, text=True)
    out.append("$ " + " ".join(cmd) + "\n" + r.stdout + r.stderr)
open("bench58_verify.txt", "w").write("\n".join(out))
