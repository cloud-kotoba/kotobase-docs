#!/usr/bin/env python3
path="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s=open(path).read()
lines=s.split("\n")
# K-Z3 line
for i,l in enumerate(lines):
    if l.startswith("| K-Z3 | worker |"):
        print("KZ3 line idx",i,"TAIL160:",repr(l[-160:]))
        break
# iterlog newest
for i,l in enumerate(lines):
    if l.strip()=="## Iteration log":
        print("HRD",i); 
        for j in range(i+1,i+4):
            print("  idx",j,":",repr(lines[j][:90]))
        break
print("total lines:",len(lines))