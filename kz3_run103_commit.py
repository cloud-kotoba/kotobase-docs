import subprocess

cmds = [
    ["git", "add", "query-cosientist.md"],
    ["git", "commit", "-m",
     "falsify 第35回: K-Z3 midnight 00h run103A-C evidence (all clean 0/20 cold, p50 0.067-0.116s, control quiet - run102A-type cluster did not recur in 2nd 00h trial; 00h band 1/4, midnight cum 23/78 ~29.5%)"],
    ["git", "push", "net-kotobase", "HEAD:main"],
]
for c in cmds:
    r = subprocess.run(c, cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs",
                       capture_output=True, text=True)
    print("$", " ".join(c))
    print(r.stdout)
    print(r.stderr)
