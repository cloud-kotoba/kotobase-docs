import subprocess
D='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
def run(cmd):
    r=subprocess.run(cmd,capture_output=True,text=True,cwd=D)
    return "CMD: "+" ".join(cmd)+"\nRC:"+str(r.returncode)+"\n"+(r.stdout or '')+(r.stderr or '')+"\n"
out=[]
out.append(run(['git','add','query-cosientist.md']))
out.append(run(['git','commit','-m','bench 第57回: K-Z3 20時台 run168A–C (cold 4/60 散発が run168A のみ, control 静穏, 20時台通算 8/300 ~2.7% 低位帯; run167 は falsify 同 tick 分と ID 衝突のため読み替え)']))
out.append(run(['git','push']))
out.append(run(['git','log','--oneline','-2']))
out.append(run(['git','status','--short','query-cosientist.md']))
open(D+'/bench57_commit_out.txt','w').write("\n=====\n".join(out))
