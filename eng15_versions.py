import subprocess, json
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine"
r = subprocess.run(["npx", "wrangler", "versions", "list", "--json"], cwd=repo, capture_output=True, text=True, timeout=120)
try:
    data = json.loads(r.stdout)
    lines = []
    for v in data:
        lines.append(json.dumps(v, ensure_ascii=False)[:400])
    open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/eng15_versions_all.txt", "w").write("\n".join(lines))
    print("total", len(data))
except Exception as e:
    open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/eng15_versions_all.txt", "w").write("ERR " + str(e) + "\n" + r.stdout[:500])
    print("parse fail")
