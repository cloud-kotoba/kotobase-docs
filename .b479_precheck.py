# -*- coding: utf-8 -*-
P="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s=open(P,encoding="utf-8").read()
lines=s.split("\n")
for i,l in enumerate(lines):
    if l.startswith("| K-Z3 | worker |"):
        print("row idx",i)
        print("row tail 400:", l[-400:])
        print("contains run477:", "run477" in l, " run478:", "run478" in l, " run479:", "run479" in l)
        break
print("---- ev anchor count ----")
ev_anchor = "15時台 (9/8) 通算 = bench run475 (7/60 帯初) + run476 (5/60) = 12/120 (~10%) 中〜高位帯候補。status 判定は rank に委ねる (rank 専門)。"
print(s.count(ev_anchor))
print("---- iter hdr ----")
print(s.count("## Iteration log\n"))
print("---- run477/478 in iter-log first 600 chars after hdr ----")
h=s.find("## Iteration log")
print(s[h:h+400])