import os
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
out = []
out.append("exists: %s" % os.path.exists(p))
out.append("access R: %s" % os.access(p, os.R_OK))
out.append("access W: %s" % os.access(p, os.W_OK))
try:
    with open(p, encoding="utf-8") as f:
        data = f.read(100)
    out.append("read ok: %r" % data[:50])
except Exception as e:
    out.append("read error: %r" % e)
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_acc_out.txt","w").write("\n".join(out))
