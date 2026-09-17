import subprocess
cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
r = subprocess.run(["git", "log", "--oneline", "-2"], capture_output=True, text=True, cwd=cwd)
print(r.stdout)
s = open(cwd + "/query-cosientist.md", encoding="utf-8").read()
i = s.find("bench 2026-09-04 (K-Z3 深夜帯 23時台 n 積み増し run101A–C")
print("evidence-in-file:", i != -1)
j = s.find("- 2026-09-04: bench 第34回")
print("log-in-file:", j != -1)
