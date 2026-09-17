import subprocess
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine"
cmds = [
 ["git", "checkout", "net-kotobase/main"],
 ["git", "log", "--oneline", "-2"],
 ["git", "status", "--short", "--untracked-files=no"],
]
out = []
for c in cmds:
    r = subprocess.run(c, cwd=repo, capture_output=True, text=True)
    out.append("$ " + " ".join(c) + "\n" + r.stdout + r.stderr)
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/eng6_state.txt", "w").write("\n".join(out))
print("ok")
