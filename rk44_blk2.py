p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = open(p, encoding="utf-8", errors="replace").read()
import re
out = []
for m in re.finditer(r"rank ブロック", txt):
    ln = txt[:m.start()].count("\n")+1
    out.append("%d: ...%s..." % (ln, txt[max(0,m.start()-100):m.start()+100].replace("\n"," ")))
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_blk2_out.txt","w").write("\n\n".join(out))
print(len(out))
