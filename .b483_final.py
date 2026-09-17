# -*- coding: utf-8 -*-
import subprocess, io
DOC="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
def run(a):
    r=subprocess.run(a,capture_output=True,cwd=DOC,text=True)
    return (r.stdout or "")+(r.stderr or "")
o=[]
o.append("HEAD="+run(["git","rev-parse","HEAD"]).strip())
o.append("REMOTE="+run(["git","rev-parse","net-kotobase/main"]).strip())
st=run(["git","status","--porcelain","--","query-cosientist.md"])
o.append("DOC_STATUS="+st.strip())
o.append("LOG:")
o.append(run(["git","log","--oneline","-4"]))
p=DOC+"/query-cosientist.md"
with io.open(p,"r",encoding="utf-8") as f:
    t=f.read()
o.append("has_1.9558=%d" % t.count("1.9558"))
o.append("has_1.1902=%d" % t.count("1.1902"))
o.append("has_run483=%d" % t.count("run483"))
o.append("has_16hr_run483=%d" % t.count("第210回, K-Z3 16時台 n 積み増し run483"))
o.append("char_len=%d" % len(t))
h=t.find("## Iteration log")
o.append("iter_log_pos=%d" % h)
o.append("iter_log_head400:"+t[h:h+400])
with open("/tmp/t_bs483_final.log","w",encoding="utf-8") as f:
    f.write("\n".join(str(x) for x in o))
print("done")