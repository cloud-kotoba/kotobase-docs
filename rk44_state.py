import subprocess
out = []
for cmd in [["git","branch","-vv","--all"],["git","log","HEAD..origin/main","--oneline"],["git","symbolic-ref","HEAD"],["git","remote","-v"]]:
    r = subprocess.run(cmd, capture_output=True, text=True)
    out.append("$ " + " ".join(cmd))
    out.append((r.stdout or "") + (r.stderr or ""))
    out.append("---")
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_state_out.txt","w").write("\n".join(out))
