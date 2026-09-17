import subprocess

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs"
out = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_f73_commit.txt"

def sh(*args):
    r = subprocess.run(args, cwd=path, capture_output=True, text=True)
    return (r.stdout + r.stderr).strip() + f" [rc={r.returncode}]"

logs = []
logs.append("add: " + sh("git", "add", "query-cosientist.md"))
logs.append("commit: " + sh("git", "commit", "-m",
    "falsify 第71回: K-Z3 6時台 run190A-C evidence 追記 (0/60, control 静穏), status 遷移なし"))
logs.append("push: " + sh("git", "push", "net-kotobase", "HEAD:main"))
logs.append("log: " + sh("git", "log", "--oneline", "-1"))

with open(out, "w", encoding="utf-8") as f:
    f.write("\n".join(logs) + "\n")
print("done")
