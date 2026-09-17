# -*- coding: utf-8 -*-
import subprocess
fn="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
data=open(fn,encoding="utf-8").read()
for pat in ["falsify 第174回","run397A","rank 第170回","bench 第178回"]:
    print(pat, data.count(pat))
# show which lines contain them (top few)
for i,ln in enumerate(data.split("\n")):
    if "第174回" in ln and "falsify" in ln:
        print("falsify174 line",i+1, repr(ln[:40]))
# check HEAD
h=subprocess.run(["git","rev-parse","HEAD"],capture_output=True,text=True,cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs").stdout.strip()
print("HEAD",h)
# is falsify173 present anywhere / is 174 committed?
out=subprocess.run(["git","show","HEAD:query-cosientist.md"],capture_output=True,text=True).stdout
print("174 in HEAD commit:", out.count("第174回"))
print("run397 in HEAD commit:", out.count("run397A"))