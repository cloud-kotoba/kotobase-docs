import re
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = open(p, encoding="utf-8").read()
idx = s.find("| K-Z3 |")
print("idx", idx)
print(s[idx:idx+400])
print("---tail---")
print(s[idx:][s[idx:].find("| open |"):(s[idx:].find("| open |")+1200)])
