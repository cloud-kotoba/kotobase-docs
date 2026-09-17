import subprocess
# Stage only the intended file, commit, push
cmds = [
    ['git', 'add', 'query-cosientist.md'],
    ['git', 'commit', '-m', 'falsify 第48回: K-Z3 12時台 n 積み増し run128A–C (0/60 完全静穏, 12時台通算 6/80 ~7.5%, bench run127A 多発型は即時非再現)'],
    ['git', 'push', 'net-kotobase', 'HEAD:main'],
]
out = open('/tmp/cp_out.txt', 'w', encoding='utf-8')
for c in cmds:
    r = subprocess.run(c, capture_output=True, text=True)
    out.write(f'=== {c[0]} {c[1][:20]} rc={r.returncode}\n{r.stdout}{r.stderr}\n')
out.close()
print('done')
