#!/usr/bin/env python3
import subprocess
def sh(c):
    r = subprocess.run(c, shell=True, capture_output=True, text=True)
    return (r.returncode, r.stdout.strip(), r.stderr.strip())
rc,remote,_ = sh('git ls-remote net-kotobase refs/heads/main')
rm = remote.split()[0] if remote.split() else None
rc,head,_ = sh('git rev-parse HEAD')
rc,lg,_ = sh('git log --oneline -3')
print('remote main =', rm)
print('HEAD        =', head)
print('MATCH       =', rm == head)
print('log:\n' + lg)
rc,out,_ = sh('git status --porcelain -- query-cosientist.md')
print('doc working clean =', (out == ''))
print('docstatus=<%s>' % out)