#!/usr/bin/env python3
import subprocess
def sh(c):
    r = subprocess.run(c, shell=True, capture_output=True, text=True)
    return (r.returncode, r.stdout.strip(), r.stderr.strip())
rc,out,err = sh('git rev-parse HEAD')
print('HEAD=', out)
rc,out,err = sh('git ls-remote net-kotobase refs/heads/main')
print('remote main=', out.split()[0] if out.split() else None)
rc,out,err = sh('git status --porcelain -- query-cosientist.md')
print('docstatus=<%s>' % out)
rc,out,err = sh('git diff --stat -- query-cosientist.md')
print('diffstat=\n' + out)