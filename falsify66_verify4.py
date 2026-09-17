import subprocess
d = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
r = subprocess.run(['git','fetch','net-kotobase'],cwd=d,capture_output=True,text=True)
print('fetch rc', r.returncode, r.stderr[:200])
for rev in ['net-kotobase/main','HEAD']:
    txt = subprocess.run(['git','show',f'{rev}:query-cosientist.md'],cwd=d,capture_output=True,text=True).stdout
    lines = txt.splitlines()
    has175 = any('run175' in l for l in lines)
    has_b60 = any('bench 第60回' in l for l in lines)
    kz3 = [l for l in lines if l.startswith('| K-Z3')]
    print(rev, 'run175:', has175, 'bench60:', has_b60, 'K-Z3 tail:', kz3[0][-150:] if kz3 else 'NONE')
print('HEAD sha:', subprocess.run(['git','rev-parse','HEAD'],cwd=d,capture_output=True,text=True).stdout)
print('main sha:', subprocess.run(['git','rev-parse','net-kotobase/main'],cwd=d,capture_output=True,text=True).stdout)
