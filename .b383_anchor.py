#!/usr/bin/env python3
txt=open('query-cosientist.md',encoding='utf-8').read()
# candidates for the end of run382 evidence in K-Z3 row
for cand in ["2 セット帯初候補","6/120 ~5.0%","帯初候補"]:
    print(repr(cand), "count=", txt.count(cand))
# show a few chars after the last occurrence of a strong candidate
import re
idx=txt.rfind("帯初候補")
print("rfind idx=",idx)
print(repr(txt[idx-30:idx+80]))