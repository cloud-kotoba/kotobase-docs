import subprocess
D='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
def run(cmd):
    r=subprocess.run(cmd, capture_output=True, text=True, cwd=D)
    return (r.stdout or '')+(('\nERR:'+r.stderr) if r.stderr.strip() else '')
out=[]
# check if fz_run167_out.txt exists (falsify may have executed already) and its content
out.append("FZ167_OUT_EXISTS:\n"+run(['ls','-la','fz_run167_out.txt']))
out.append("FZ167_OUT_CONTENT:\n"+run(['cat','fz_run167_out.txt']))
# check fz_run166.sh existence and content, and run166 occurrences
out.append("GREP run166:\n"+run(['grep','-n','run166','query-cosientist.md']))
# 20時台 historical totals: grep for 20時台 通算
out.append("GREP 20時台通算:\n"+run(['grep','-n','20時台通算','query-cosientist.md']))
open(D+'/bench57_ids2.txt','w').write("\n=====\n".join(out))
