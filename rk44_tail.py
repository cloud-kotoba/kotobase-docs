p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = open(p, encoding="utf-8", errors="replace").read()
tail = txt[-6000:]
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_tail_out.txt","w").write(tail)
print("ok")
