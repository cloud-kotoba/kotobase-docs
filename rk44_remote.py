import subprocess, json, os
out = []
# check for new remote branches / commits beyond 8847fdd
for cmd in [["git","log","--oneline","-8","net-kotobase/main"],["git","branch","-r"]]:
    r = subprocess.run(cmd, capture_output=True, text=True, cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
    out.append("$ " + " ".join(cmd))
    out.append(r.stdout + r.stderr)
    out.append("---")
# check remote branch cosient-20260905-run123-obs tip vs main
r = subprocess.run(["git","log","--oneline","-2","net-kotobase/cosient-20260905-run123-obs"], capture_output=True, text=True, cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
out.append("$ branch obs tip"); out.append(r.stdout + r.stderr)
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_remote_out.txt","w").write("\n".join(out))
print("ok")
