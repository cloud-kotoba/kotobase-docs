import subprocess, re
env = {"GIT_DIR": "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/.git",
       "PATH": "/usr/bin:/bin:/usr/local/bin:/opt/homebrew/bin", "HOME": "/Users/junkawasaki"}
# built artifact at 7dc6249 — does it contain the summary fn logic (e.g. ";distinct=")?
r = subprocess.run(["git", "show", "7dc6249:js/kotobase-graph-database-worker.js"],
                   capture_output=True, text=True, timeout=30, env=env)
s = r.stdout
for pat in ["distinct=", ";b2=", "block-fetch", "fetch-block-cached"]:
    idx = s.find(pat)
    print(pat, "first at", idx)
    if idx >= 0:
        print(repr(s[idx-100:idx+100]))
