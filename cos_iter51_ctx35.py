import re, glob
# The kotobase.net edge: which repo serves it? control-plane? search for "kotobase.net" route bindings
for f in glob.glob("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/*/wrangler*.json*"):
    s = open(f).read()
    if "kotobase.net" in s:
        hits = [m.group(0) for m in re.finditer(r'[^",]*kotobase\.net[^",]*', s)]
        print(f.split("orgs/net-kotobase/")[1], hits[:6])
