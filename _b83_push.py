import subprocess
msg = 'bench 83: K-Z3 13時台 run210A-C evidence (cold 6/60, run210A冒頭集中型, control分離)'
r = subprocess.run(['git', 'add', 'query-cosientist.md'], capture_output=True, text=True)
r2 = subprocess.run(['git', 'commit', '-m', msg], capture_output=True, text=True)
out = (r.stdout + r.stderr + '||' + r2.stdout + r2.stderr)
r3 = subprocess.run(['git', 'push', 'net-kotobase', 'HEAD:main'], capture_output=True, text=True)
out += '||' + r3.stdout + r3.stderr + '||rc_push=' + str(r3.returncode)
open('_b83_push_out.txt', 'w').write(out + '\n')
