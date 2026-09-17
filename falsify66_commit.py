import subprocess
d = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
out = []
def run(*args):
    r = subprocess.run(args, cwd=d, capture_output=True, text=True)
    out.append('$ ' + ' '.join(args))
    out.append(r.stdout)
    out.append(r.stderr)
    out.append('rc=' + str(r.returncode))
run('git', 'add', 'query-cosientist.md')
run('git', '-c', 'user.name=net-kotobase-falsify', '-c', 'user.email=falsify@net-kotobase.local',
    'commit', '-m', 'falsify 67: K-Z3 23時台 run175A-C 0/60 cold, control 静穏; K-Q1 deploy run 33964821723 queued 滞留継続確認')
run('git', 'push', 'net-kotobase', 'HEAD:main')
open(d + '/falsify66_commit_out.txt', 'w').write('\n'.join(out))
