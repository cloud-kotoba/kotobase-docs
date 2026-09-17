import subprocess
def run(cmd):
    p = subprocess.run(["bash","-lc",cmd], capture_output=True, text=True,
        cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/control-plane")
    return (p.stdout + p.stderr).strip()
out=[]
out.append("main bundle grep: "+run("git grep -c 'x-kotobase-kv-stats' origin/main -- 'kotobase-api-gateway/js/kotobase-worker.js' 'kotobase-api-gateway/js/*' || echo NOMATCH"))
out.append("main log: "+run("git log --oneline -4 origin/main"))
out.append("bf630923 ancestor: "+run("git merge-base --is-ancestor bf630923 origin/main && echo YES || echo NO"))
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/pr615_out2.txt","w").write("\n".join(out))
