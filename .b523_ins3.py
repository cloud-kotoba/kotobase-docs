#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io, unicodedata
D="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/"
P=D+"query-cosientist.md"
ev=io.open(D+".b523_EV.txt",encoding="utf-8").read().rstrip("\n")
ilog=io.open(D+".b523_IL.txt",encoding="utf-8").read().rstrip("\n")
def clean(s):
    s=s.replace("\u200b","").replace("\u200c","").replace("\u200d","").replace("\ufeff","")
    return "".join([ch for ch in s if unicodedata.combining(ch)==0])
ev=clean(ev)
ilog=clean(ilog)
s=io.open(P,encoding="utf-8").read()
lines=s.split("\n")
idx=None
for i,l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        idx=i
        break
assert idx is not None, "no K-Z3 row"
text="\n".join(lines)
assert "第233回" not in text
lines[idx]=lines[idx]+ev
news="\n".join(lines)
anchor="## Iteration log\n"
ia=news.find(anchor)
assert ia!=-1,"no iter header"
news=news[:ia+len(anchor)]+ilog+news[ia+len(anchor):]
news=clean(news)
cnt=news.count("第233回")
assert cnt==2,"cnt233=%d"%cnt
w=io.open(P,"w",encoding="utf-8",newline="")
w.write(news)
w.close()
print("OK row",idx+1,"iter",ia,"len",len(news),"cnt",cnt)