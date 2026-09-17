import subprocess

repo = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
cmds = [
    ['git', 'add', 'query-cosientist.md', 'bench59_run172.sh', 'bench59_run172_out.txt', 'bench59_stats.py', 'bench59_stats.json', 'bench59_append.py'],
    ['git', 'commit', '-m', 'bench 第59回: K-Z3 22時台初計測 run172A-C (cold 3/2/0 = 5/60, control 静穏)'],
    ['git', 'push', 'origin', 'HEAD'],
]
for c in cmds:
    r = subprocess.run(c, cwd=repo, capture_output=True, text=True)
    print(' '.join(c), '-> rc', r.returncode)
    if r.stdout.strip():
        print(r.stdout[-500:])
    if r.returncode != 0 and r.stderr.strip():
        print(r.stderr[-800:])
