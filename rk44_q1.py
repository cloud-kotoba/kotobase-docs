p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = open(p, encoding="utf-8", errors="replace").read()
lines = txt.splitlines()
out = []
out.append("=== K-Q1 row L52 tail 12000 ===")
out.append(lines[51][-12000:])
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_q1_out.txt","w").write("\n".join(out))
print("ok")
