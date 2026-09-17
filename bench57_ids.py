import subprocess
D='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
def run(cmd):
    r=subprocess.run(cmd, capture_output=True, text=True, cwd=D)
    return (r.stdout or '')+(('\nERR:'+r.stderr) if r.stderr.strip() else '')
out=[]
out.append("GREP run167 in md:\n"+run(['grep','-n','run167','query-cosientist.md']))
out.append("GREP run168 in md:\n"+run(['grep','-n','run168','query-cosientist.md']))
out.append("GREP run169 in md:\n"+run(['grep','-n','run169','query-cosientist.md']))
out.append("LINES 808-830:\n"+run(['sed','-n','808,830p','query-cosientist.md']))
out.append("LINES 760,777 (run89 area):\n"+run(['sed','-n','760,777p','query-cosientist.md']))
open(D+'/bench57_ids.txt','w').write("\n=====\n".join(out))
