import subprocess
def run(*a):
    p = subprocess.run(a, capture_output=True, text=True)
    return p.returncode, (p.stdout+p.stderr).strip()
print('push', run('git','push','net-kotobase','HEAD:refs/heads/main'))
print('fetch', run('git','fetch','net-kotobase'))
print('remote main', run('git','rev-parse','net-kotobase/main'))
print('HEAD', run('git','rev-parse','HEAD'))
