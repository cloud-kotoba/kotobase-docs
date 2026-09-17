p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = open(p, encoding="utf-8", errors="replace").read()
lines = txt.split("\n")
out = []
for idx in range(164, 201):
    out.append("%d: %s" % (idx+1, lines[idx][:400]))
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_rank2_out.txt","w").write("\n".join(out))
print("ok")
