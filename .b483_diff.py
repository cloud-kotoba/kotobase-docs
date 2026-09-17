# -*- coding: utf-8 -*-
import subprocess, io
DOC = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/"
r = subprocess.run(["git","-C",DOC,"diff","HEAD","--","query-cosientist.md"],
                   capture_output=True)
out = r.stdout.decode("utf-8", errors="replace")
with io.open("/tmp/t_bs483_mydiff.log","w",encoding="utf-8") as f:
    f.write("LEN=%d\n" % len(out))
    f.write(out)
print("diff_len=%d bytes" % len(out))