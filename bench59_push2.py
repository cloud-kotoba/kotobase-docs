import subprocess

repo = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
for c in [['git', 'branch', '--show-current'], ['git', 'push', 'net-kotobase', 'main:main'], ['git', 'log', '--oneline', '-1']]:
    r = subprocess.run(c, cwd=repo, capture_output=True, text=True)
    print(' '.join(c), '-> rc', r.returncode)
    print(r.stdout.strip()[-400:], r.stderr.strip()[-400:])
