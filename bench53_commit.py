import subprocess

cmds = ['git add query-cosientist.md',
        'git commit -m "bench 第53回: K-Z3 18時台 n 積み増し run161A-C (search cold 1/60, p50 40-56ms, control 静穏, run158 型全体遅延窓非再現, 18時台通算 4/180 ~2.2% 低位帯) evidence + iteration log 追記 — status 遷移なし"',
        'git push net-kotobase HEAD:main']
out = open('bench53_commit_out.txt', 'w')
for c in cmds:
    r = subprocess.run(c, shell=True, capture_output=True, text=True)
    out.write(f'$ {c}\nrc={r.returncode}\n{r.stdout}{r.stderr}\n')
out.close()
