import subprocess
D='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
def run(cmd):
    r=subprocess.run(cmd,capture_output=True,text=True,cwd=D)
    return "CMD: "+" ".join(cmd)+"\nRC:"+str(r.returncode)+"\n"+(r.stdout or '')+(r.stderr or '')+"\n"
out=[]
out.append(run(['git','push','net-kotobase','HEAD:main']))
out.append(run(['git','log','--oneline','-1']))
open(D+'/bench57_push2.txt','w').write("\n=====\n".join(out))
