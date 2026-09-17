p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = open(p, encoding="utf-8", errors="replace").read()
res = []
import re
for m in re.finditer(r"run125", txt):
    ln = txt[:m.start()].count("\n")+1
    res.append("line %d" % ln)
res.append("count: %d" % txt.count("run125"))
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_chk_out.txt","w").write("\n".join(res))
