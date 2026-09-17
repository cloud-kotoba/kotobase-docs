import subprocess, os
os.chdir("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
def sh(c,t=120):
    r=subprocess.run(c,shell=True,capture_output=True,text=True,timeout=t)
    return f"$ {c}\n[r={r.returncode}]\nOUT:{r.stdout}\nERR:{r.stderr}"
out=[]
# check how previous rank pushed - look at reflog/remote state
out.append(sh("git push net-kotobase HEAD:refs/heads/main 2>&1"))
out.append(sh("git fetch net-kotobase && git rev-parse net-kotobase/main"))
open("/tmp/_push.txt","w").write("\n".join(out))
print("pushed")