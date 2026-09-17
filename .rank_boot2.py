import subprocess, os
os.chdir("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
out = []
def sh(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    return f"$ {cmd}\n[r={r.returncode}]\n{r.stdout}{r.stderr}"
for c in [
    "git rev-parse HEAD",
    "git log --oneline -8",
    "git status --short",
    "git branch -vv",
]:
    out.append(sh(c))
open("/tmp/_rank_boot_out.txt","w").write("\n\n"+"="*60+"\n\n".join(out))
print("WROTE")