p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = open(p, encoding="utf-8", errors="replace").read()
# rank block = population section. 第43回版 mentions around line 1281 are iteration log. 
# The actual "rank ブロック" is presumably the population table itself (updated each rank iteration).
# Check line counts around 200 and look for a dedicated rank summary block maybe in population section end (before line 200 note).
# Print lines 100-140 quickly? Instead find "第43回版" in population section (before line 202)
lines = txt.split("\n")
out = []
for idx, ln in enumerate(lines[:201]):
    if "第43回版" in ln or "第43回" in ln:
        out.append("HIT %d: %s" % (idx+1, ln[:250]))
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_blk3_out.txt","w").write("\n".join(out))
print("ok")
