# -*- coding: utf-8 -*-
import subprocess, io
DOC="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
def run(a):
    r=subprocess.run(a,capture_output=True,cwd=DOC,text=True)
    return (r.stdout or "")+(r.stderr or "")
o=[]
o.append("HEAD="+run(["git","rev-parse","HEAD"]).strip())
o.append("REMOTE="+run(["git","rev-parse","net-kotobase/main"]).strip())
o.append("DOC_STATUS="+run(["git","status","--porcelain","--","query-cosientist.md"]).strip())
o.append("LOG:")
o.append(run(["git","log","--oneline","-4"]))
p=DOC+"/query-cosientist.md"
with io.open(p,"r",encoding="utf-8") as f:
    t=f.read()
o.append("len=%d" % len(t))
o.append("run484A=%d" % t.count("run484A"))
o.append("1.9558=%d" % t.count("1.9558"))
o.append("has_210_entry=%d" % t.count("bench 第210回。16:54"))
# is my evidence still in the file?
o.append("has_27/360=%d" % t.count("27/360"))
o.append("has_25/300=%d" % t.count("25/300"))
h=t.find("## Iteration log")
o.append("--- iter head 500 ---")
o.append(t[h:h+500])
with open("/tmp/t_bs483_cur.log","w",encoding="utf-8") as f:
    f.write("\n".join(str(x) for x in o))
print("done")