p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = open(p, encoding="utf-8", errors="replace").read()
lines = txt.split("\n")
# show lines 176-202 (population tail: notes under table, maybe rank block)
out = []
for idx in range(174, 205):
    if idx < len(lines):
        out.append("%d: %s" % (idx+1, lines[idx][:250]))
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_sec2_out.txt","w").write("\n".join(out))
print("ok")
