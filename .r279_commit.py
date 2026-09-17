import subprocess as sp
cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
def sh(c, **kw):
    r = sp.run(c, shell=True, cwd=cwd, capture_output=True, text=True, **kw)
    return (r.stdout + r.stderr)
out = sh("git commit -m 'rank 279: K-Z3 9/16 deep-night 2 run fold (run635 3時台, run630 5時台), K-Z4 3日系列 2帯追加, NEXT run637 7時台'")
out += "---PUSH---\n" + sh("git push bench_fetch HEAD:main") + sh("git push net-kotobase HEAD:main")
out += "---POST---\n"
pushed = sh("git show bench_fetch/main:query-cosientist.md | grep -c 'rank 第279回。'")
out += "remote grep rank279: " + pushed
sp.run("git rev-parse HEAD > .r279_final_rev.txt", shell=True, cwd=cwd)
open(cwd+"/.r279_commit_out.txt","w").write(out)
