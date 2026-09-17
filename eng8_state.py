import subprocess
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine"
cmds = [
 ["git", "stash", "push", "-m", "cosient49: stray artifact diff before deploy sync"],
 ["git", "status", "--short", "--untracked-files=no"],
 ["git", "log", "--oneline", "-1"],
]
out = []
for c in cmds:
    r = subprocess.run(c, cwd=repo, capture_output=True, text=True)
    out.append("$ " + " ".join(c) + "\n" + r.stdout + r.stderr)
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/eng8_state.txt", "w").write("\n".join(out))
print("ok")
