import subprocess
out = subprocess.run(["git", "show", "3e2bff3", "query-cosientist.md"], cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs", capture_output=True, text=True)
lines = [l for l in out.stdout.splitlines() if "run169" in l]
with open("/tmp/cos58_f64.txt", "w") as f:
    f.write("\n".join(lines[:10]))
print("lines:", len(lines))
