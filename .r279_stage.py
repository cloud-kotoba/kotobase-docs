import subprocess as sp
# verify staged content before commit (reverse-variant recovery lesson)
sp.run("git add query-cosientist.md", shell=True, cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs", capture_output=True)
staged = sp.run("git show :query-cosientist.md", shell=True, cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs", capture_output=True, text=True).stdout
ok = "rank 第279回。" in staged and staged.count("## Iteration log") == 1
with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.r279_verify.txt","w") as f:
    f.write("staged entry present: %s ; headers: %d\n" % (ok, staged.count("## Iteration log")))
