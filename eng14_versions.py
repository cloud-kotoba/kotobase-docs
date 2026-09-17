import subprocess, json
repo = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/engine"
r = subprocess.run(["npx", "wrangler", "versions", "list", "--json"], cwd=repo, capture_output=True, text=True, timeout=120)
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/eng14_versions_raw.txt", "w").write("RC=%d\n" % r.returncode + r.stdout[:4000] + r.stderr[:1000])
try:
    data = json.loads(r.stdout)
    lines = []
    for v in data[:6]:
        lines.append(json.dumps({k: v.get(k) for k in ("id", "number", "created", "source", "tag")}, ensure_ascii=False))
    open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/eng14_versions.txt", "w").write("\n".join(lines))
    print("parsed", len(data))
except Exception as e:
    print("parse fail", e)
