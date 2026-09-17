#!/usr/bin/env python3
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b390_rank164.py"
lines=open(p,"r",encoding="utf-8").read().split("\n")
out=[]
for ln in lines:
    out.append(ln)
    if ln.strip().startswith("f.write(out)"):
        break
open(p,"w",encoding="utf-8").write("\n".join(out)+"\n")
open("/tmp/b390_trim.txt","w").write("trimmed lines=%d\n" % len(out))