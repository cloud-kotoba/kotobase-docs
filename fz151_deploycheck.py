import subprocess
# K-Q1 deploy check: x-kotobase-kv-stats header presence on search.kotobase.net (1 request)
out = subprocess.run(
    ["curl", "-s", "-D", "-", "-o", "/dev/null",
     "https://search.kotobase.net/search?q=test"],
    capture_output=True, text=True, timeout=30).stdout
with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/fz151_deploycheck.txt", "w") as f:
    f.write(out)
print("written", len(out))
