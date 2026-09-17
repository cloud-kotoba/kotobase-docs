import subprocess
r = subprocess.run(["git","diff","--stat"], capture_output=True, text=True,
                   cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
out = [r.stdout + r.stderr]
r2 = subprocess.run(["git","diff","query-cosientist.md"], capture_output=True, text=True,
                    cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
out.append(r2.stdout)
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_diff_out.txt","w").write("\n".join(out))
print("ok")
