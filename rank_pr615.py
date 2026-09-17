import subprocess
def run(args, cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/control-plane"):
    p = subprocess.run(args, capture_output=True, text=True, cwd=cwd)
    return p.stdout + p.stderr
out = []
out.append("== fetch ==\n"+run(["git","fetch","origin","--prune"]))
out.append("== PR615 branch ancestry ==\n"+run(["bash","-lc",
  "git rev-parse origin/main; git branch -a --list '*kq1-bundle-rebuild*'; "
  "git merge-base --is-ancestor origin/bot/cosient-20260905-kq1-bundle-rebuild origin/main && echo ANCESTOR-YES || echo ANCESTOR-NO"]))
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/pr615_out.txt","w").write("\n".join(out))
