import subprocess
out = []
for cmd in [["git","fetch","net-kotobase"],["git","log","--oneline","-3","net-kotobase/main"],["git","rev-parse","HEAD","net-kotobase/main"],["git","diff","--stat","HEAD","net-kotobase/main","--","query-cosientist.md"]]:
    r = subprocess.run(cmd, capture_output=True, text=True, cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
    out.append("$ " + " ".join(cmd))
    out.append((r.stdout or "") + (r.stderr or ""))
    out.append("---")
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_fetch_out.txt","w").write("\n".join(out))
