import subprocess, re
env = {"GIT_DIR": "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/.git",
       "PATH": "/usr/bin:/bin:/usr/local/bin:/opt/homebrew/bin", "HOME": "/Users/junkawasaki"}
r = subprocess.run(["git", "show", "7dc6249:src/kotobase/graph_database/store.cljs"],
                   capture_output=True, text=True, timeout=30, env=env)
s = r.stdout
# show the summary fn and where record-block-fetch calls are anchored (which stage branches)
for m in re.finditer(r'record-block-fetch!', s):
    print("---", m.start())
    print(s[m.start()-120:m.start()+60].replace("\n", " | ")[-170:])
