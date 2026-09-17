import os, glob, datetime, re
d = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine"
for f in glob.glob(d + "/**/wrangler*.toml", recursive=True) + glob.glob(d + "/**/wrangler*.json*", recursive=True):
    print("config:", f.replace(d + "/", ""))
    s = open(f).read()
    for line in s.splitlines():
        if re.match(r'\s*(name|main)\s*=', line):
            print("   ", line.strip())
