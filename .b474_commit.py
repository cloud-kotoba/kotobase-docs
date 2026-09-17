#!/usr/bin/env python3
import subprocess
cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
def sh(cmd):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=90)
    return (r.returncode, r.stdout.strip(), r.stderr.strip())
out = []
# stage only the evidence file (not scratch)
rc, so, se = sh(["git", "add", "query-cosientist.md"])
out.append("add_rc=%d %s" % (rc, se))
msg = "falsify 213: K-Z3 14h n-add run474 cold 3/60 ~5.0% (run474A 2+C 1 散発即消失; 14h total 22/300 ~7.3% 5set; control 境界1 borderline note)"
rc, so, se = sh(["git", "commit", "-m", msg])
out.append("commit_rc=%d %s" % (rc, se))
rc, so, se = sh(["git", "rev-parse", "HEAD"])
out.append("newhead=%s" % so)
# push detached HEAD
rc, so, se = sh(["git", "push", "net-kotobase", "HEAD:main"])
out.append("push_rc=%d %s" % (rc, so + " " + se))
open("/tmp/commit474.txt", "w", encoding="utf-8").write("\n".join(out) + "\n")
print("ok")