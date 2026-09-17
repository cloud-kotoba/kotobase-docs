import subprocess
p = subprocess.run(["wc", "-l", "query-cosientist.md"], capture_output=True, text=True, cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
print(p.stdout.strip())
# print lines 112-139 exactly
with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md") as f:
    lines = f.readlines()
print(len(lines))
