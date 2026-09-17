import subprocess as sp
cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
def sh(c):
    return sp.run(c, shell=True, cwd=cwd, capture_output=True, text=True).stdout
out=[]
out.append("HEAD: "+sh("git rev-parse HEAD"))
out.append("log: "+sh("git log --oneline -3"))
wt=open(cwd+"/query-cosientist.md",encoding="utf-8").read()
out.append("worktree has rank279: %s ; headers: %d" % ("rank 第279回。" in wt, wt.count("## Iteration log")))
out.append("HEAD blob has rank279: %s" % ("rank 第279回。" in sh("git show HEAD:query-cosientist.md")))
open(cwd+"/.r279_diag.txt","w").write("\n".join(out))
