import subprocess
env = {"GIT_DIR": "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/.git",
       "PATH": "/usr/bin:/bin:/usr/local/bin:/opt/homebrew/bin", "HOME": "/Users/junkawasaki"}
r = subprocess.run(["git", "show", "7dc6249:src/kotobase/graph_database/store.cljs"],
                   capture_output=True, text=True, timeout=30, env=env)
s = r.stdout
for name in ["block-fetch-stats", "record-block-fetch", "block-fetch-stats-summary", "reset-block-fetch-stats"]:
    print(name, s.count(name))
