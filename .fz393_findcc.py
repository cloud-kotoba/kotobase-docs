#!/usr/bin/env python3
path = "query-cosientist.md"
s = open(path, encoding="utf-8").read()
idx = s.find("run393A\u2013C\u2013C")
print("CC idx:", idx)
print(repr(s[idx-80:idx+40]))
# also check iter-log entry for same issue
i2 = s.find("run393A\u2013C\u2013C", idx+1)
print("2nd:", i2, repr(s[i2-80:i2+40]) if i2>0 else "-")