import subprocess, json, os
p = subprocess.run(["bash","-lc","gh run view 33964821723 --repo net-kotobase/control-plane --json status,conclusion,updatedAt,headSha,displayTitle 2>&1"],
  capture_output=True, text=True)
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/gh_run_out.txt","w").write(p.stdout+p.stderr)
