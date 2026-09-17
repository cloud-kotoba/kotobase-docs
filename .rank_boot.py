import subprocess, os
os.chdir("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
def sh(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return f"$ {cmd}\n{'-'*40}\n[r={r.returncode}]\nSTDOUT:\n{r.stdout}\nSTDERR:\n{r.stderr}"
for c in [
    "git rev-parse HEAD",
    "git log --oneline -8",
    "git status --short",
    "git branch -vv",
]:
    print(sh(c))