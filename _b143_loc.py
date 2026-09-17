#!/usr/bin/env python3
path="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s=open(path).read()
lines=s.split("\n")
# locate K-Z3 evidence row (lines 0-based)
for i,l in enumerate(lines):
    if l.startswith("| K-Z3 | worker |"):
        print("KZ3 line idx(0-based)=",i,"(1-based line",i+1,")")
        print("TAIL80:",repr(l[-80:]))
        break
# locate iteration log header
for i,l in enumerate(lines):
    if l.strip()=="## Iteration log":
        print("ITERLOG header idx=",i,"(1-based",i+1,")")
        print("next line idx=",i+1,":",repr(lines[i+1][:120]))
        break
print("total lines:",len(lines))