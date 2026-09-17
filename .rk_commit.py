import subprocess, os
os.chdir("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
def sh(c,t=90):
    r=subprocess.run(c,shell=True,capture_output=True,text=True,timeout=t)
    return f"$ {c}\n[r={r.returncode}]\nOUT:{r.stdout}\nERR:{r.stderr}"
out=[]
out.append(sh("git add query-cosientist.md && git commit -m 'rank 113: fold bench104 run258A-C cold 3/60 ~5.0% (early-head small cluster, B/C 0/20 vanish, control sep, heavy 6/20-grade not reproduced in 4 sets + this), 22hr total 25/420 ~6.0%, status/rank unchanged, NEXT K-Z3 23hr band-first'"))
out.append(sh("git fetch net-kotobase && git rev-parse net-kotobase/main && git rev-parse HEAD"))
open("/tmp/_commit.txt","w").write("\n".join(out))
print("committed")