import subprocess

cwd = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
r = subprocess.run(["git", "add", "query-cosientist.md"], cwd=cwd,
                   capture_output=True, text=True)
r2 = subprocess.run(["git", "commit", "-m",
                     "bench 第35回: K-Z3 深夜帯 0時台 run104A-C evidence 追記"],
                    cwd=cwd, capture_output=True, text=True)
with open("kz3_run104_commit_out.txt", "w", encoding="utf-8") as f:
    f.write("add rc=%s\ncommit rc=%s\n%s\n%s\n" % (r.returncode, r2.returncode,
                                                   r2.stdout, r2.stderr))
print("ok")
