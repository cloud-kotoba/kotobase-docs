import subprocess
cmds = [
 ["git", "status", "--short", "--untracked-files=no"],
 ["git", "log", "--oneline", "-2"],
 ["git", "branch", "-a", "--list", "*cosient*"],
]
out = []
for c in cmds:
    r = subprocess.run(c, cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine", capture_output=True, text=True)
    out.append("$ " + " ".join(c) + "\n" + r.stdout + r.stderr)
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/eng5_state.txt", "w").write("\n".join(out))
print("ok")
