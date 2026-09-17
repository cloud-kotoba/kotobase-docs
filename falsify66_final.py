import subprocess
d = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
subprocess.run(['git','fetch','net-kotobase'],cwd=d,capture_output=True,text=True)
txt = subprocess.run(['git','show','net-kotobase/main:query-cosientist.md'],cwd=d,capture_output=True,text=True).stdout
lines = txt.splitlines()
kz3 = [l for l in lines if l.startswith('| K-Z3')]
res = ['push sha:', subprocess.run(['git','rev-parse','net-kotobase/main'],cwd=d,capture_output=True,text=True).stdout.strip()]
res.append('run175 in main K-Z3: ' + str('run175' in kz3[0]))
res.append('K-Z3 tail: ' + kz3[0][-400:])
open(d+'/falsify66_final_verify.txt','w').write('\n'.join(res))
