import subprocess
# stage and commit only query-cosientist.md
cmds = [
    ['git', 'add', 'query-cosientist.md'],
    ['git', 'commit', '-m',
     'falsify 第63回: K-Z3 20時台帯初計測 run167A-C (cold 0/60, control 同時上振れで partially not-separated) evidence 追記'],
    ['git', 'push', 'net-kotobase', 'HEAD:main'],
]
out = []
for c in cmds:
    r = subprocess.run(c, capture_output=True, text=True)
    out.append(f"$ {' '.join(c)}\nrc={r.returncode}\nSTDOUT:\n{r.stdout}\nSTDERR:\n{r.stderr}\n")
open('fz63_git_out.txt', 'w').write('\n'.join(out))
print('done')
