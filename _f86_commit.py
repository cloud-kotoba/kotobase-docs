import io, subprocess

docs = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/'

def sh(cmd):
    p = subprocess.run(cmd, shell=True, cwd=docs, capture_output=True, text=True)
    return (p.stdout or '') + (p.stderr or '')

with io.open(docs + '_f86_commit.txt', 'w', encoding='utf-8') as f:
    f.write(sh('git add query-cosientist.md && git commit -m "falsify 86: K-Z3 14時台帯初 run212A-C evidence (cold 4/60, run212A 冒頭集中型) + iteration log 追記"'))
    f.write('\n---\n')
    f.write(sh('git rev-parse HEAD'))
