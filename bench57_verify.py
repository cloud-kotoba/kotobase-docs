import subprocess
D='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
def run(cmd):
    r=subprocess.run(cmd,capture_output=True,text=True,cwd=D)
    return "RC:"+str(r.returncode)+"\n"+(r.stdout or '')+(r.stderr or '')
out=[]
out.append("TAILLOG:\n"+run(['tail','-c','600','query-cosientist.md']))
out.append("GREP run168 count:\n"+run(['grep','-c','run168','query-cosientist.md']))
out.append("STATUS:\n"+run(['git','status','--short']))
open(D+'/bench57_verify.txt','w').write("\n=====\n".join(out))
