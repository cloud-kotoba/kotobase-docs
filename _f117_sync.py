import subprocess
subprocess.run(['git','fetch','net-kotobase'],cwd='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs',capture_output=True)
subprocess.run(['git','checkout','net-kotobase/main'],cwd='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs',capture_output=True)
p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
lines=open(p,encoding='utf-8').readlines()
idx=[i for i,l in enumerate(lines) if '| K-Z3 |' in l][0]
import re
r256=[i for i,l in enumerate(lines) if re.search(r'run256',l)]
r255=[i for i,l in enumerate(lines) if re.search(r'run255',l)]
head=subprocess.run(['git','rev-parse','HEAD'],cwd='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs',capture_output=True,text=True).stdout.strip()
log=subprocess.run(['git','log','--oneline','-2'],cwd='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs',capture_output=True,text=True).stdout
with open('/tmp/f117_sync.txt','w') as f:
    f.write("HEAD=%s\nKZ3_idx=%d\nrun256_hits=%d at %s\nrun255_hits=%d\n%s\n" % (head, idx, len(r256), r256[:5], len(r255), log))
print("OK")