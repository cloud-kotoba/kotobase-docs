p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = open(p, encoding="utf-8", errors="replace").read()
lines = txt.split("\n")
# Examine the K-Q1 hypothesis description and status cell boundary: extract full row with status field
row = lines[51]
# status is field 4 (index 3) within '| ... | ... | ... | open | evidence'
parts = row.split(" | ")
out = ["n_parts=%d" % len(parts)]
out.append("status part: %s" % parts[3][:120])
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_row_out.txt","w").write("\n".join(out))
# Also print end of the K-Q1 evidence (last 500 chars of row)
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_row_tail_out.txt","w").write(row[-600:])
print("ok")
