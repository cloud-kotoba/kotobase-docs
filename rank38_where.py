import sys
out = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rank38_out11.txt','w')
sys.stdout = out
import os
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
txt = open('query-cosientist.md', encoding='utf-8').read()
lines = txt.splitlines()
print('worktree lines:', len(lines), 'bytes:', len(txt.encode('utf-8')))
# Where is run106 and run107 evidence
for i, l in enumerate(lines):
    if 'run106' in l or 'run107' in l:
        print(i+1, ':', l[:180])
out.close()
