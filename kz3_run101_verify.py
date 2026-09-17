import subprocess

p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
out = subprocess.run(["git", "diff", "--stat", "--", "query-cosientist.md"],
                     capture_output=True, text=True, cwd="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs")
print(out.stdout, out.stderr)

s = open(p, encoding="utf-8").read()
for needle in ["run101A–C", "bench 第34回", "K-Z3 深夜帯 23時台 n 積み増し継続。"]:
    print(needle, "->", s.count(needle))
# no secrets check (basic)
import re
for pat in ["token", "cookie", "credential", "Bearer "]:
    hits = re.findall(pat, s, re.I)
    if hits:
        print("WARN secret-like:", pat, len(hits))
print("total chars:", len(s))
