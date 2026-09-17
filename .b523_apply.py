#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io, unicodedata
D="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/"
P=D+"query-cosientist.md"
EV=io.open(D+".b523_EV.txt",encoding="utf-8").read().strip()
IL=io.open(D+".b523_IL.txt",encoding="utf-8").read().strip()
def clean(s):
    s=s.replace("\u200b","").replace("\u200c","").replace("\u200d","").replace("\ufeff","")
    return "".join([ch for ch in s if unicodedata.combining(ch)==0])
EV=clean(EV)
IL=clean(IL)
fl=io.open(P,encoding="utf-8",newline="").readlines()
hdrs=[i for i,l in enumerate(fl) if "## Iteration log" in l]
kz=[i for i,l in enumerate(fl) if l.startswith("| K-Z3 |")]
assert hdrs
assert kz
text="".join(fl)
assert "第233回" not in text
hi=hdrs[0]; ki=kz[0]
row=fl[ki]
assert row.endswith("\n")
core=row[:-1]
fl[ki]=core+" "+EV+"\n"
assert fl[hi].startswith("## Iteration log")
fl.insert(hi+1, IL+"\n")
out=clean("".join(fl)
cnt=out.count("第233回")
assert cnt==2
w=io.open(P,"w",encoding="utf-8",newline="")
w.write(out
w.close()
print("OK")
print(ki+1)
print(hi+2)
print(len(out)
print(cnt)