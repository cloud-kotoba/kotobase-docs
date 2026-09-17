import subprocess
d='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
msg=("falsify: K-Z3 11時台 n 積み増し run127A-C (11:16 JST, cold 0/60 完全静穏, control 静穏 — bench 第46回 run126 10/60 と正反対で 11時台通算 10/120 は 1 セットのみの寄与, 帯内突発性が再確認, traffic 依存説判定は対称 2 サンプルに) — status 判定は rank に委ねる")
r=subprocess.run(['git','add','query-cosientist.md','fz_run127.sh','fz_run127_out.txt','fz127_append.py','fz127_inspect.py','fz127_tailcheck.py'],cwd=d,capture_output=True,text=True)
r2=subprocess.run(['git','commit','-m',msg],cwd=d,capture_output=True,text=True)
r3=subprocess.run(['git','push','net-kotobase','HEAD:main'],cwd=d,capture_output=True,text=True)
open('/tmp/fz127_git.txt','w').write("ADD:%s\nCOMMIT:%s\nPUSH:%s\n"%(r.stdout[-200:]+r.stderr[-200:],r2.stdout[-300:]+r2.stderr[-300:],r3.stdout[-300:]+r3.stderr[-300:]))
