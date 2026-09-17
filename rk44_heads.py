import re
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = open(p, encoding="utf-8", errors="replace").read()
res = []
for m in re.finditer(r"^#{1,4} .*$',?$", txt, re.M):
    pass
res = []
for m in re.finditer(r"(?m)^#{1,4}[ \t].*$", txt):
    ln = txt[:m.start()].count("\n")+1
    res.append("%d: %s" % (ln, m.group(0)))
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_heads_out.txt","w").write("\n".join(res))
print(len(res))
