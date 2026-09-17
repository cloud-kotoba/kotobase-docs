import subprocess
def run(*a):
    p = subprocess.run(a, capture_output=True, text=True)
    return p.returncode, p.stdout.strip(), p.stderr.strip()
print('fetch', run('git','fetch','net-kotobase'))
print('main', run('git','rev-parse','net-kotobase/main'))
print('HEAD', run('git','rev-parse','HEAD'))
print('anc', run('git','merge-base','--is-ancestor','HEAD','net-kotobase/main'))
