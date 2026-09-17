#!/usr/bin/env python3
import subprocess
cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
def sh(cmd):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, timeout=90)
    return (r.returncode, r.stdout.strip(), r.stderr.strip())
out = []
rc, so, se = sh(["git", "fetch", "net-kotobase"])
out.append("fetch_rc=%d %s" % (rc, se))
rc, so, _ = sh(["git", "rev-parse", "HEAD"])
out.append("local=%s" % so)
rc, so, _ = sh(["git", "rev-parse", "net-kotobase/main"])
out.append("nk=%s" % so)
rc, so, _ = sh(["git", "log", "net-kotobase/main", "--oneline", "-3"])
out.append("nklog=" + so.replace("\n", " | "))
open("/tmp/post474.txt", "w", encoding="utf-8").write("\n".join(out) + "\n")
print("ok")