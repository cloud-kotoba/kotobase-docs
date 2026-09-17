import subprocess, sys

PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

subprocess.run(["git", "add", PATH], cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs", check=True)
msg = ("bench 第49回: K-Q1 deploy 判別再確認 (PR#3 merge 7dc6249 済みだが production header 不在 6/6, "
       "deployed:false) + transact 401 新規継続を記録 + 空 graph warm query p50 299.94/309.81ms (not-separated)")
subprocess.run(["git", "commit", "-m", msg], cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs", check=True)
subprocess.run(["git", "push", "net-kotobase", "HEAD:main"], cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs", check=True)
print("committed and pushed")
