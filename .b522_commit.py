#!/usr/bin/env python3
import subprocess
def sh(c):
    r = subprocess.run(c, shell=True, capture_output=True, text=True)
    return (r.returncode, r.stdout.strip(), r.stderr.strip())
rc,out,err = sh('git add query-cosientist.md')
print('add rc=', rc, err)
rc,out,err = sh('git commit -m "falsify 232: K-Z3 1hr n-add run522 cold 6/60 ~10.0 pct control 2/20 not-separated (run521 taken by bench223 -> read替 run522)"')
print('commit rc=', rc)
print('out=', out[:500])
print('err=', err[:500])