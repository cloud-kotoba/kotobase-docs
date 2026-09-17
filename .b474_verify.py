#!/usr/bin/env python3
import subprocess, sys
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
data = open(path, encoding="utf-8").read()
out = []
out.append("zwnbsp_count=%d" % sum(1 for c in data if ord(c) in (0x200b, 0x200c, 0x200d, 0xfeff)))
out.append("hash5_count=%d" % data.count("#####"))
out.append("run474_count=%d" % data.count("run474"))
out.append("falsify213_count=%d" % data.count("第213回"))
# file size
import os
out.append("filesize=%d" % os.path.getsize(path))
# git diffstat via subprocess (may be slow)
r = subprocess.run(["git", "diff", "--stat"], cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs",
                   capture_output=True, text=True, timeout=60)
out.append("DIFFSTAT:")
out.append(r.stdout[:2000])
out.append("diffstat_rc=%d" % r.returncode)
open("/tmp/verify474.txt", "w", encoding="utf-8").write("\n".join(out) + "\n")
print("written")