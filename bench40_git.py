import subprocess
d = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
r = subprocess.run(["git","add","query-cosientist.md"], cwd=d, capture_output=True, text=True)
r2 = subprocess.run(["git","commit","-m","bench 第40回: K-Z3 深夜帯 6時台 run115A-C (cold 0/60, 完全静穏, control 静穏) — evidence 追記"], cwd=d, capture_output=True, text=True)
r3 = subprocess.run(["git","push"], cwd=d, capture_output=True, text=True)
out = open(d + "/bench40_git.txt","w")
out.write("add: %s %s\ncommit: %s %s\npush: %s %s\n" % (r.returncode, r.stdout[-200:], r2.returncode, (r2.stdout+r2.stderr)[-300:], r3.returncode, (r3.stdout+r3.stderr)[-300:]))
out.close()
