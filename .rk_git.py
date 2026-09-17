import subprocess, os
os.chdir("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
def sh(c):
    r=subprocess.run(c,shell=True,capture_output=True,text=True)
    return f"$ {c}\n[r={r.returncode}]\n{r.stdout}{r.stderr}"
out=[]
out.append(sh("git show 968b4c5 --stat"))
out.append(sh("git show 968b4c5 --format= -- query-cosientist.md | head -40"))
out.append(sh("git show 1768f6e --stat"))
out.append(sh("git show 1768f6e --format= -- query-cosientist.md | grep -c 'run258'"))
open("/tmp/_gitconf.txt","w").write("\n".join(out))
print("ok")