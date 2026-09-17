import subprocess
D='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
def run(cmd):
    r=subprocess.run(cmd,capture_output=True,text=True,cwd=D)
    return "CMD: "+" ".join(cmd)+"\nRC:"+str(r.returncode)+"\n"+(r.stdout or '')+(r.stderr or '')+"\n"
out=[]
out.append(run(['git','branch','--show-current']))
out.append(run(['git','remote','-v']))
out.append(run(['git','log','--oneline','origin/main','-1']))
out.append(run(['git','rev-parse','HEAD']))
open(D+'/bench57_branch.txt','w').write("\n=====\n".join(out))
