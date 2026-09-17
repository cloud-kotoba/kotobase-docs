import subprocess
env = {"GIT_DIR": "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/.git",
       "PATH": "/usr/bin:/bin:/usr/local/bin:/opt/homebrew/bin", "HOME": "/Users/junkawasaki"}
r = subprocess.run(["git", "log", "--oneline", "-5", "--", "js/kotobase-graph-database-worker.js"],
                   capture_output=True, text=True, timeout=30, env=env)
print(r.stdout)
r2 = subprocess.run(["git", "log", "-1", "--format=%ci", "7dc6249", "--", "js/kotobase-graph-database-worker.js"],
                    capture_output=True, text=True, timeout=30, env=env)
print("artifact last touched:", r2.stdout)
