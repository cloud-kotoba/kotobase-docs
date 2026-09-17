import subprocess, json, time
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine"
out = []
r = subprocess.run(["npx", "wrangler", "versions", "list"], cwd=repo, capture_output=True, text=True, timeout=120)
out.append("$ wrangler versions list\n" + r.stdout[-2000:] + r.stderr[-500:])
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/eng13_versions.txt", "w").write("\n".join(out))
print("ok")
