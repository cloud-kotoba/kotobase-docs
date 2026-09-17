import subprocess, os
os.chdir("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
def sh(c):
    r=subprocess.run(c,shell=True,capture_output=True,text=True)
    return f"$ {c}\n[r={r.returncode}]\n{r.stdout}{r.stderr}"
out=[]
out.append(sh("grep -c '第113回' query-cosientist.md"))
out.append(sh("grep -c '25/420' query-cosientist.md"))
out.append(sh("grep -n 'rank (期待 gain' query-cosientist.md | head"))
out.append(sh("sed -n '251,253p' query-cosientist.md"))
out.append(sh("sed -n '303,307p' query-cosientist.md"))
out.append(sh("git diff --stat"))
open("/tmp/_verify.txt","w").write("\n".join(out))
print("ok")