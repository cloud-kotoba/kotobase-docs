import subprocess
D='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
def run(cmd):
    r=subprocess.run(cmd, capture_output=True, text=True, cwd=D)
    return (r.stdout or '')+(('\nERR:'+r.stderr) if r.stderr.strip() else '')
out=[]
# find all runs with 20:xx JST timestamps (20時台)
out.append("GREP 20:xx JST:\n"+run(['grep','-n','20:[0-9][0-9] JST','query-cosientist.md']))
open(D+'/bench57_ids3.txt','w').write("\n=====\n".join(out))
