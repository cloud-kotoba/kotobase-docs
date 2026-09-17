p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = open(p, encoding="utf-8", errors="replace").read()
lines = txt.splitlines()
out = []
# K-Q1 row (L52) full text, K-Z3 row tail (L175) full
out.append("=== K-Q1 row (L52) full ===")
out.append(lines[51])
out.append("")
out.append("=== K-Z2 row (L110) tail 2000 ===")
out.append(lines[109][-2000:])
out.append("")
out.append("=== K-Z3 row (L175) tail 3000 ===")
out.append(lines[174][-3000:])
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_rows_out.txt","w").write("\n".join(out))
print("ok")
