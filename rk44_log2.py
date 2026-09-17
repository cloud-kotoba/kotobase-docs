p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = open(p, encoding="utf-8", errors="replace").read()
idx = txt.find("## Iteration log")
out = ["index: %d, char pos: %d" % (txt.count("## Iteration log"), idx)]
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_log2_out.txt","w").write(out[0])
# find all headings
import re
for m in re.finditer(r"^## .*$", txt, re.M):
    out.append("%d: %s" % (txt[:m.start()].count("\n")+1, m.group(0)))
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_log2_out.txt","w").write("\n".join(out))
print("ok")
