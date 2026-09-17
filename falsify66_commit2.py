import subprocess
d = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
out = []
def run(*args):
    r = subprocess.run(args, cwd=d, capture_output=True, text=True)
    out.append('$ ' + ' '.join(args[:5]))
    out.append((r.stdout + r.stderr).strip()[:800])
    out.append('rc=' + str(r.returncode))
run('git', 'add', 'query-cosientist.md')
run('git', '-c', 'user.name=net-kotobase-falsify', '-c', 'user.email=falsify@net-kotobase.local',
    'commit', '-m', 'falsify 67 fix: K-Z3 K-Z3 run175 evidence 追記修正 (前 commit で差分取り消しになっていた分を正しく追記)')
run('git', 'push', 'net-kotobase', 'HEAD:main')
open(d + '/falsify66_commit2_out.txt', 'w').write('\n'.join(out))
