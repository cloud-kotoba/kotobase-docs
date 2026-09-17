import subprocess, os
os.chdir("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
out=[]
def sh(cmd, t=60):
    try:
        r=subprocess.run(cmd,shell=True,capture_output=True,text=True,timeout=t)
        return f"$ {cmd}\n[r={r.returncode}]\nOUT:\n{r.stdout}\nERR:\n{r.stderr}"
    except Exception as e:
        return f"$ {cmd}\n[EXC] {e}"
out.append(sh("git rev-parse HEAD"))
out.append(sh("git fetch --all --prune 2>&1; git remote -v"))
out.append(sh("git status --short --branch | head -5"))
out.append(sh("git log --oneline -15"))
out.append(sh("grep -n '' query-cosientist.md | wc -l"))
open("/tmp/_rk_state.txt","w").write("\n\n"+"="*70+"\n".join(out))
print("OK")