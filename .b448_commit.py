#!/usr/bin/env python3
import subprocess
def run(cmd, out):
    r = subprocess.run(cmd, capture_output=True, text=True, cwd='.')
    open(out, 'a').write('$ ' + ' '.join(cmd) + '\nRC=' + str(r.returncode) + '\n' + (r.stdout or '') + (r.stderr or '') + '\n')
    return r.returncode
run(['git', 'add', 'query-cosientist.md'], '/tmp/b448_git.txt')
run(['git', 'commit', '-m', 'bench 第200回: K-Z3 9時台 n-add run448 cold 2/60 ~3.3% (control 完全静穏分離成立); evidence + iter-log'], '/tmp/b448_git.txt')
run(['git', 'rev-parse', 'HEAD'], '/tmp/b448_git.txt')
run(['git', 'log', '--oneline', '-1'], '/tmp/b448_git.txt')
print('done')