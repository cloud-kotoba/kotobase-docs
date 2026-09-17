import subprocess
d = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
out = []
def run(*args):
    r = subprocess.run(args, cwd=d, capture_output=True, text=True)
    out.append('$ ' + ' '.join(args[:4]))
    out.append((r.stdout + r.stderr).strip()[:500])
    out.append('rc=' + str(r.returncode))
# check diff only touches K-Z3 line
run('git', 'diff', '--stat')
run('git', 'diff', '-U0')
open(d + '/falsify66_fix_diff.txt', 'w').write('\n'.join(out))
