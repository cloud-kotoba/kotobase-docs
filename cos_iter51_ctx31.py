import subprocess
env = {"GIT_DIR": "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/.git",
       "PATH": "/usr/bin:/bin:/usr/local/bin:/opt/homebrew/bin", "HOME": "/Users/junkawasaki"}
r = subprocess.run(["git", "show", "7dc6249:src/kotobase/graph_database/xrpc.cljs"],
                   capture_output=True, text=True, timeout=30, env=env)
s = r.stdout
# print the context of the 2 assoc-response-kv-stats call sites fully
i1 = s.find("assoc-response-kv-stats", 15000)
print("CALL1 around", i1)
print(s[i1-600:i1+300])
print("=====")
i2 = s.find("assoc-response-kv-stats", 16500)
print("CALL2 around", i2)
print(s[i2-700:i2+400])
