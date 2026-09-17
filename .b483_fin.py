# -*- coding: utf-8 -*-
import subprocess, io
DOC="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
def run(a):
    r=subprocess.run(a,capture_output=True,cwd=DOC,text=True)
    return (r.stdout or "")+(r.stderr or "")
o=[]
o.append("HEAD="+run(["git","rev-parse","HEAD"]).strip())
o.append("REMOTE="+run(["git","rev-parse","net-kotobase/main"]).strip())
o.append("STATUS_DOC="+run(["git","status","--porcelain","--","query-cosientist.md"]).strip())
o.append("LOG3:")
o.append(run(["git","log","--oneline","-3"]))
# verify content present
p=DOC+"/query-cosientist.md"
with io.open(p,"r",encoding="utf-8") as f:
    t=f.read()
o.append("run484A=%d 1.9558=%d 27/360=%d" % (t.count("run484A"),t.count("1.9558"),t.count("27/360")))
o.append("iter_entry_ok=%d" % t.count("- 2026-09-08: bench 第210回。16:54 JST tick"))
with open("/tmp/t_bs483_fin.log","w",encoding="utf-8") as f:
    f.write("\n".join(str(x) for x in o))
print("done")