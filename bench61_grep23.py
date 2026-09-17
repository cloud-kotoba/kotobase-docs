import re
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = open(p, encoding="utf-8").read()
# find all "23時台" mentions with context
for m in re.finditer("23時台", s):
    a = max(0, m.start()-160)
    b = min(len(s), m.end()+240)
    print("...", s[a:b].replace("\n", " "), "...")
    print("=====")
