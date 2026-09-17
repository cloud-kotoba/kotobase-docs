import subprocess, re
env = {"GIT_DIR": "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/.git",
       "PATH": "/usr/bin:/bin:/usr/local/bin:/opt/homebrew/bin", "HOME": "/Users/junkawasaki"}
r = subprocess.run(["git", "show", "7dc6249:js/kotobase-graph-database-worker.js"],
                   capture_output=True, text=True, timeout=30, env=env)
s = r.stdout
i = s.find("kv=")
print(repr(s[i-200:i+200]))
