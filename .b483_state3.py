# -*- coding: utf-8 -*-
import subprocess, io
DOC="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
def run(a):
    r=subprocess.run(a,capture_output=True,cwd=DOC)
    return r.stdout.decode("utf-8",errors="replace")
out=[]
out.append("HEAD="+run(["git","rev-parse","HEAD"]).strip())
out.append("REMOTE="+run(["git","rev-parse","net-kotobase/main"]).strip())
out.append("BRANCH="+run(["git","branch","-a"]).strip())
out.append("--- log -5 ---")
out.append(run(["git","log","--oneline","-5"]).strip())
out.append("--- status ---")
out.append(run(["git","status","--short"]).strip())
data="\n".join(out)
with io.open("/tmp/t_bs483_state3.log","w",encoding="utf-8") as f:
    f.write(data)
print("written")