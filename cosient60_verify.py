import subprocess
r = subprocess.run(["grep", "-n", "run173A", "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"],
                   capture_output=True, text=True)
print(r.stdout[:400])
