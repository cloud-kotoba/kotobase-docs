import subprocess
env = {"GIT_DIR": "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/.git",
       "PATH": "/usr/bin:/bin:/usr/local/bin:/opt/homebrew/bin", "HOME": "/Users/junkawasaki"}
r = subprocess.run(["git", "show", "7dc6249:src/kotobase/graph_database/xrpc.cljs"],
                   capture_output=True, text=True, timeout=30, env=env)
s = r.stdout
i = s.find("assoc-response-kv-stats")
print("first assoc def at", i)
# Is the reset call present anywhere? reset-block-fetch-stats!
print("reset count:", s.count("reset-block-fetch-stats"))
print("record count:", s.count("record-block-fetch"))
