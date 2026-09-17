p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = open(p, encoding="utf-8", errors="replace").read()
# context around 第43回版 at 117299
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk43ctx_out.txt","w").write(txt[117299-2500:117299+800])
# also find rank block heading like "## rank ブロック" or "rank block"
import re
for m in re.finditer(r"^#+ .*rank.*$", txt, re.M | re.I):
    print(txt[:m.start()].count("\n")+1, m.group(0))
