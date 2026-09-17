# -*- coding: utf-8 -*-
import io, re
p = "/Users/junkawasaki/github/com/junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
txt = io.open(p, encoding="utf-8").read()
lines = txt.split("\n")
# find iter log header
for i, ln in enumerate(lines, 1):
    if ln.startswith("## Iteration log"):
        print("ITERLOG_HEADER_LINE", i)
        # print first 12 entries after header
        cnt = 0
        for j in range(i, min(len(lines), i+60)):
            s = lines[j].strip()
            if s.startswith("- "):
                print(j+1, "|", s[:170])
                cnt += 1
                if cnt >= 8:
                    break
        break
print("---NEXT mentions (last 5)---")
for tok in ["NEXT:", "NEXT (", "委ねる"]:
    print("===", tok)
    idxs = [i for i, ln in enumerate(lines, 1) if tok in ln]
    for k in idxs[-3:]:
        print(k, "|", lines[k-1][:200])