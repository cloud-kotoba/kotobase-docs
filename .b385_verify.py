#!/usr/bin/env python3
import io
path="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s=io.open(path,encoding="utf-8").read()
lines=s.split("\n")
for i,l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        print("TAIL_L%d="%(i+1)+l[-500:])
        break
an="## Iteration log\n"
ia=s.find(an)
print("ITER_FIRST_ENTRY:")
print(s[ia:ia+1500])