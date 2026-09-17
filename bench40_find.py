import re
doc = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md", encoding="utf-8").read()
out = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench40_find.txt","w", encoding="utf-8")
for i, line in enumerate(doc.splitlines(), 1):
    if re.search(r"K-Z[123]|NEXT|quiet-host", line):
        out.write("%d: %s\n" % (i, line[:600]))
out.close()
