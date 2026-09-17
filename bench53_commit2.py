import subprocess

cmds = ['git add query-cosientist.md',
        'git commit -m "bench 第53回追記修正: iteration log 挿入位置を bench 第52回行直前に修正 (rank 第52回エントリの分断解消) + falsify 第59回 (別インスタンス同時実行) との run161 ID 衝突注記を evidence/log 両方に追記"',
        'git push net-kotobase HEAD:main']
out = open('bench53_commit2_out.txt', 'w')
for c in cmds:
    r = subprocess.run(c, shell=True, capture_output=True, text=True)
    out.write(f'$ {c}\nrc={r.returncode}\n{r.stdout}{r.stderr}\n')
out.close()
