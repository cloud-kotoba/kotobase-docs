p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = open(p, encoding="utf-8", errors="replace").read()
i = txt.find("| bench 2026-09-05 (第39回")
out = ["pos: %d" % i]
print(i)
# K-Q1 rank block: search for 'rank 第43回版' or the rank block description
import re
for pat in ["rank 第40回版", "第43回版", "## rank", "### rank"]:
    j = txt.find(pat)
    out.append("%s -> %d" % (pat, j))
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_blk_out.txt","w").write("\n".join(out))
