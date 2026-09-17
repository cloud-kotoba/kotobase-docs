# -*- coding: utf-8 -*-
fn="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
data=open(fn,encoding="utf-8").read()
for bad in ["\u200b","\u200c","\u200d"]:
    data=data.replace(bad,"")
lines=data.split("\n")

# load evidence text from out-of-band ev file to avoid inline escaping
ev=open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.f397_ev.txt",encoding="utf-8").read().rstrip("\n")
it=open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.f397_it.txt",encoding="utf-8").read().rstrip("\n")

kidx=278
assert lines[kidx].startswith("| K-Z3 |"), lines[kidx][:30]
lines[kidx]=lines[kidx]+" "+ev

hidx=None
for i,ln in enumerate(lines):
    if ln.strip()=="## Iteration log":
        hidx=i
        break
assert hidx is not None, "iter head missing"
lines.insert(hidx+1, it)

open(fn,"w",encoding="utf-8").write("\n".join(lines))
comb="\n".join(lines)
print("OK kidx=%d hidx=%d"%(kidx,hidx))
print("run397A count",comb.count("run397A"))
print("falsify 第174 count",comb.count("第174回"))
print("ev len",len(ev),"it len",len(it))