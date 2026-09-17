import subprocess, io, os
os.chdir("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
out = io.open("bench68_commit_out.txt", "w", encoding="utf-8")
def run(cmd):
    r = subprocess.run(cmd, shell=True, capture_output=True, text=True)
    out.write("$ %s\nrc=%d\n%s\n%s\n" % (cmd, r.returncode, r.stdout, r.stderr))
    return r.returncode

run("git add query-cosientist.md bench68_kz3_5am.mjs bench68_kz3_5am_out.json")
run('git commit -m "docs: falsify 第68回 evidence — K-Z3 5時台 1セット目 run185A-C (cold 0/60 完全静穏, 低位帯下限側) + iteration log"')
run("git push net-kotobase HEAD:main")
run("git log --oneline -2")
out.close()
