import subprocess
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine"
r = subprocess.run(["git", "diff", "--stat", "js/kotobase-graph-database-worker.js"], cwd=repo, capture_output=True, text=True)
out = r.stdout + r.stderr
r2 = subprocess.run(["git", "log", "--oneline", "-3", "--all", "--source", "--", "js/kotobase-graph-database-worker.js"], cwd=repo, capture_output=True, text=True)
out += "\n" + r2.stdout + r2.stderr
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/eng7_state.txt", "w").write(out)
print("ok")
