import subprocess
out = []
# new commits on remote not yet in local log file (falsify run after eee3314): 8847fdd
# read the diff of 8847fdd to see what evidence it added
for cmd in [["git","show","8847fdd","--stat"],["git","show","8847fdd","--","query-cosientist.md"]]:
    r = subprocess.run(cmd, capture_output=True, text=True, cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
    out.append("$ " + " ".join(cmd))
    out.append((r.stdout or "") + (r.stderr or ""))
    out.append("---")
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_show_out.txt","w").write("\n".join(out))
