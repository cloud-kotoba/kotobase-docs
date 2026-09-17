#!/usr/bin/env python3
# report cold positions for run478
THRESH = 0.5
base = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b478"
out = []
for k in ["A","B","C","landing"]:
    vals = [(i+1,float(x)) for i,x in enumerate(open(base+"_"+k+".ttfb").read().split()) if x.strip()]
    c = ["%d:%.4f"%(i,v) for i,v in vals if v >= THRESH]
    out.append("RUN%s coldpos=%s"%(k,",".join(c)))
print("\n".join(out))
with open("/tmp/b478_pos.txt","w",encoding="utf-8") as f:
    f.write("\n".join(out)+"\n")