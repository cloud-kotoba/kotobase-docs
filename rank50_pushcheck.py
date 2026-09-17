#!/usr/bin/env python3
import subprocess
r = subprocess.run(["git", "log", "--oneline", "-2", "net-kotobase/main"],
                   capture_output=True, text=True,
                   cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
open("/tmp/rank50_push.txt", "w").write(r.stdout + r.stderr)
print(r.stdout + r.stderr)
