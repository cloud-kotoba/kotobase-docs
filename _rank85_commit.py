#!/usr/bin/env python3
# verify append + commit + push
import io, subprocess, sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    txt = f.read()

ok = "rank 第85回" in txt and "NEXT: K-Z3 13時台 n 積み増し (前回指定の継続" in txt
print("verify_append:", ok)
print("lines:", txt.count("\n"))
if not ok:
    sys.exit(1)

cmds = [
    ["git", "add", "query-cosientist.md"],
    ["git", "commit", "-m", "rank 第85回: 新規 evidence 0 本, rank 更新なし, NEXT K-Z3 13時台 n 積み増し継続"],
    ["git", "push", "net-kotobase", "HEAD:main"],
]
for c in cmds:
    r = subprocess.run(c, capture_output=True, text=True)
    print(" ".join(c), "rc=", r.returncode)
    if r.stdout.strip():
        print(r.stdout.strip()[:500])
    if r.returncode != 0:
        print(r.stderr.strip()[:500])
        sys.exit(1)
print("done")
