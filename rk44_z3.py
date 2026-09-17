p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = open(p, encoding="utf-8", errors="replace").read()
i = txt.index("| K-Z3 |")
seg = txt[i:i+60000]
j = seg.index("| open |")
rest = seg[j+len("| open |"):]
k = rest.find("\n\n")
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_z3_out.txt","w").write(rest[:k])
print(len(rest[:k]))
