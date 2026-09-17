p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = open(p, encoding="utf-8", errors="replace").read()
lines = txt.split("\n")
# lines 44-200 (0-indexed 43-199) — the population section body, look for rank block structure
out = []
for idx in range(43, 60):
    out.append("%d: %s" % (idx+1, lines[idx][:200]))
out.append("...")
# find lines mentioning "rank 第43回" within population section
for idx in range(47, 201):
    if "rank 第43回" in lines[idx] or "rank block" in lines[idx] or "rank ブロック" in lines[idx]:
        out.append("HIT %d: %s" % (idx+1, lines[idx][:300]))
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_sec_out.txt","w").write("\n".join(out))
print("ok")
