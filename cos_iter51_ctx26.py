import os, re
d = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine"
for f in ["js/kotobase-graph-database-worker.js"]:
    st = os.stat(os.path.join(d, f))
    import datetime
    print(f, "mtime:", datetime.datetime.fromtimestamp(st.st_mtime))
w = open(os.path.join(d, "wrangler.toml")).read()
for line in w.splitlines():
    if re.match(r'\s*(name|main|workers_dev|route|compatibility_date)', line):
        print("wrangler.toml:", line.strip())
