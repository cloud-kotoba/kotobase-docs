import subprocess
out = []
# Confirm working tree is clean wrt tracked files, and confirm HEAD == net-kotobase/main == 8847fdd
for cmd in [["git","status","--porcelain","--","query-cosientist.md"],["git","rev-parse","HEAD"],["git","stash","list"]]:
    r = subprocess.run(cmd, capture_output=True, text=True, cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
    out.append("$ " + " ".join(cmd) + " -> " + repr((r.stdout or "") + (r.stderr or "")))
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_wc_out.txt","w").write("\n".join(out))
print("ok")
