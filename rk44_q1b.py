p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = open(p, encoding="utf-8", errors="replace").read()
# K-Q1 row: split on '| K-Q1 |' then next '| open |'
i = txt.index("| K-Q1 |")
seg = txt[i:i+25000]
j = seg.index("| open |")
out = ["=== K-Q1 evidence field (between '| open |' and next '||'/row end) ==="]
rest = seg[j+len("| open |"):]
# row ends at next line starting with newline then '| K-' or blank line; capture until '\n\n'
k = rest.find("\n\n")
out.append(rest[:k])
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_q1b_out.txt","w").write(out[0]+"\n"+rest[:k])
print(len(rest[:k]))
