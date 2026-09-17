#!/usr/bin/env python3
import re
path = "query-cosientist.md"
s = open(path, encoding="utf-8").read()
for m in re.finditer(r"[\u200b\u200c\u200d\ufeff]", s):
    print("zwsp at byte-pos", m.start(), "context:", repr(s[max(0,m.start()-25):m.start()+10]))
print("---")
# check my run393 evidence region specifically
i = s.find("第168回")
print("run393 evidence region zwsp:", len(re.findall(r"[\u200b\u200c]", s[i:i+2500])))