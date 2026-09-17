#!/usr/bin/env python3
import subprocess
def run(cmd, out):
    r = subprocess.run(cmd, capture_output=True, text=True, cwd='.')
    open(out, 'a').write('$ ' + ' '.join(cmd) + '\nRC=' + str(r.returncode) + '\n' + (r.stdout or '') + (r.stderr or '') + '\n')
    return r.returncode
run(['git', 'push', 'net-kotobase', 'HEAD:main'], '/tmp/b448_push.txt')
run(['git', 'rev-parse', 'HEAD'], '/tmp/b448_push.txt')
run(['git', 'rev-parse', 'net-kotobase/main'], '/tmp/b448_push.txt')
print('done')