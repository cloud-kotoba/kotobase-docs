import subprocess
def run(*a):
    p = subprocess.run(a, capture_output=True, text=True)
    return p.returncode, (p.stdout+p.stderr).strip()
print('lsremote', run('git','ls-remote','net-kotobase'))
print('retry push', run('git','push','net-kotobase','HEAD:refs/heads/net-kotobase/main'))
