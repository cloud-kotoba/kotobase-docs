p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = open(p, encoding="utf-8", errors="replace").read()
lines = txt.splitlines()
# Iteration log section: find last entries. Find index of "## Iteration log"
i = txt.index("## Iteration log")
out = ["total lines: %d, Iteration log at line %d" % (len(lines), i+1)]
out.extend(lines[i+1:i+40])
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rk44_log_out.txt","w").write("\n".join(out))
print("ok")
