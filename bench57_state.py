import subprocess, sys, os
D='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
r = subprocess.run(['wc','-l',D+'/query-cosientist.md'], capture_output=True, text=True)
r2 = subprocess.run(['grep','-n','NEXT','DUMMY'], capture_output=True, text=True)
# gather: file size, grep for 要 quiet-host, NEXT occurrences, hypothesis rows
def run(cmd):
    return subprocess.run(cmd, capture_output=True, text=True, cwd=D)
lines=[]
lines.append("WC:"+run(['wc','-l','query-cosientist.md']).stdout)
lines.append("GREP_QUIETHOST:\n"+run(['grep','-n','要 quiet-host','query-cosientist.md']).stdout)
lines.append("GREP_NEXT_HEAD:\n"+"\n".join(run(['grep','-n','NEXT','query-cosientist.md']).stdout.strip().split("\n")[-12:]))
lines.append("GREP_KZ3:\n"+run(['grep','-n','K-Z3','query-cosientist.md']).stdout)
lines.append("GREP_KQ1:\n"+run(['grep','-n','K-Q1','query-cosientist.md']).stdout)
lines.append("GREP_HEADER:\n"+run(['grep','-n','x-kotobase-kv-stats','query-cosientist.md']).stdout)
lines.append("LS:\n"+"\n".join(sorted(os.listdir(D))))
with open(D+'/bench57_state.txt','w') as f:
    f.write("\n=====\n".join(lines))
