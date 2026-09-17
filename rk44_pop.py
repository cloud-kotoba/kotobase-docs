import re
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = open(p, encoding="utf-8", errors="replace").read()
lines = txt.splitlines()
out = []
# Find hypothesis table rows (K-xx) and hypothesis population section
in_pop = False
for i, ln in enumerate(lines):
    if "hypothesis population" in ln.lower():
        in_pop = True
        out.append(">>> population section starts line %d: %s" % (i+1, ln))
    if re.search(r"\| K-[A-Z][0-9]", ln):
        out.append("L%d: %s" % (i+1, ln[:1500]))
        out.append("")
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_pop_out.txt","w").write("\n".join(out))
print("done")
