#!/usr/bin/env python3
import subprocess
def sh(c):
    r = subprocess.run(c, shell=True, capture_output=True, text=True)
    return (r.returncode, r.stdout.strip(), r.stderr.strip())
rc,remote,_ = sh('git ls-remote net-kotobase refs/heads/main')
rm = remote.split()[0] if remote.split() else None
rc,head,_ = sh('git rev-parse HEAD')
print('remote main =', rm)
print('HEAD        =', head)
rc,out,_ = sh('git merge-base --is-ancestor %s %s && echo FFOK || echo NOTFF' % (rm, head))
print(out)
rc,out,err = sh('git push net-kotobase HEAD:main')
print('push rc=', rc)
print('push out=', out[:800])
print('push err=', err[:400])