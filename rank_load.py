import subprocess, re
p = subprocess.run(["bash","-lc","uptime"], capture_output=True, text=True)
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/load_out.txt","w").write(p.stdout+p.stderr)
