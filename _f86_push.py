import io, subprocess

docs = '/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/'

def sh(cmd):
    p = subprocess.run(cmd, shell=True, cwd=docs, capture_output=True, text=True)
    return (p.stdout or '') + (p.stderr or '')

with io.open(docs + '_f86_push.txt', 'w', encoding='utf-8') as f:
    f.write(sh('git push net-kotobase HEAD:main'))
    f.write('\n---\n')
    f.write(sh('git fetch net-kotobase && git rev-parse net-kotobase/main'))
