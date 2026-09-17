import json, re
s = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine/wrangler.jsonc").read()
# strip // comments crudely for main/name fields
for line in s.splitlines():
    if re.search(r'"(name|main)"\s*:', line):
        print(line.strip()[:120])
