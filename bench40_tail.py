lines = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md", encoding="utf-8").read().splitlines()
out = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench40_tail.txt","w", encoding="utf-8")
# print from the rank 第39回 entry to end of iteration log section
import re
start = None
for i,l in enumerate(lines):
    if "bench 第39回" in l and l.startswith("- 2026"):
        start = i
out.write("start=%d total=%d\n" % (start, len(lines)))
for i in range(start, min(start+40, len(lines))):
    out.write("%d: %s\n" % (i+1, lines[i][:1500]))
out.close()
