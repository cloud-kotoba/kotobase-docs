import subprocess, re
env = {"GIT_DIR": "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/.git",
       "PATH": "/usr/bin:/bin:/usr/local/bin:/opt/homebrew/bin", "HOME": "/Users/junkawasaki"}
r = subprocess.run(["git", "show", "7dc6249:src/kotobase/graph_database/xrpc.cljs"],
                   capture_output=True, text=True, timeout=30, env=env)
s = r.stdout
i = s.find("assoc-response-kv-stats", 12000)
j = s.find("(defn- assoc-response-kv-stats")
print("def at", j)
print(s[j:j+600])
# reset placement
k = s.find("reset-block-fetch-stats!")
print("reset call at", k)
print(s[k-500:k+120])
