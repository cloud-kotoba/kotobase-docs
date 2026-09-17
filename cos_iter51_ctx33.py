import subprocess
env = {"GIT_DIR": "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/.git",
       "PATH": "/usr/bin:/bin:/usr/local/bin:/opt/homebrew/bin", "HOME": "/Users/junkawasaki"}
r = subprocess.run(["git", "show", "7dc6249:src/kotobase/graph_database/worker.cljs"],
                   capture_output=True, text=True, timeout=30, env=env)
s = r.stdout
import re
for m in re.finditer(r'headers\.set|new Response|\$headers', s):
    pass
# how does frontend/proxy interplay? just count occurrences of x-kotobase-request-id
print("request-id set:", s.count("x-kotobase-request-id"))
# check kv-stats in worker.cljs
print("kv-stats in worker.cljs:", s.count("kv-stats"))
