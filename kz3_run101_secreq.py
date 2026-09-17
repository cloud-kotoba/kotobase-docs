import re
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = open(p, encoding="utf-8").read()
for m in re.finditer(r"token|cookie|credential", s, re.I):
    a = max(0, m.start()-60)
    print(repr(s[a:m.end()+60]))
