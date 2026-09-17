#!/usr/bin/env python3
import subprocess
cmds = [
    ["git", "push", "bench_fetch", "HEAD:main"],
]
for c in cmds:
    r = subprocess.run(c, capture_output=True, text=True)
    with open("/tmp/rank_push.txt", "w", encoding="utf-8") as f:
        f.write("CMD: %s\nEXIT=%d\nSTDOUT:%s\nSTDERR:%s\n" % (c, r.returncode, r.stdout, r.stderr))
print("push done")