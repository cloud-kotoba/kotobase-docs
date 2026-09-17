#!/usr/bin/env python3
path="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s=open(path).read()
lines=s.split("\n")
print("line359 =", lines[358][:60])
print("line359 contains run334A:", "run334A" in lines[358])
l279=lines[278]
print("line279 len:", len(l279))
print("line279 contains run334 2/60:", "run334" in l279 and "2/60" in l279)
print("line279 tail:", l279[-120:])