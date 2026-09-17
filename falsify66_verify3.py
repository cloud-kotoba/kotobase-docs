import subprocess
d = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
txt = subprocess.run(['git','show','HEAD:query-cosientist.md'],cwd=d,capture_output=True,text=True).stdout
lines = txt.splitlines()
hits = [(i+1, l[:100]) for i,l in enumerate(lines) if 'run175' in l]
kz3 = [ (i+1, l[-500:]) for i,l in enumerate(lines) if l.startswith('| K-Z3') ]
open(d+'/falsify66_verify3.txt','w').write('run175 hits: %s\n\nK-Z3 lines: %d\n' % (hits, len(kz3)))
for n, t in kz3:
    open(d+'/falsify66_verify3.txt','a').write('\nline %d tail:\n%s\n' % (n, t))
