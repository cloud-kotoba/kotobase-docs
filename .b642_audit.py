import io, subprocess

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
head_blob = subprocess.run(
    ["git", "-C", "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs",
     "show", "HEAD:query-cosientist.md"],
    capture_output=True).stdout.decode("utf-8", "replace")

with io.open(path, "r", encoding="utf-8") as fh:
    now = fh.read()

for label, t in [("HEAD(pre-edit)", head_blob), ("NOW(post-edit)", now)]:
    print(label, "158th:", t.count("\u7b2c158\u56de"),
          "157th:", t.count("\u7b2c157\u56de"),
          "run642:", t.count("run642"),
          "run643:", t.count("run643"))

# where does 'falsify 第158回' occur in NOW?
lines = now.split("\n")
hits = [i for i, ln in enumerate(lines) if "falsify \u7b2c158\u56de" in ln]
print("NOW lines with 'falsify 第158回':", hits[:20], "total", len(hits))
for i in hits[:15]:
    pos = lines[i].find("falsify \u7b2c158\u56de")
    print(f"  L{i+1} len={len(lines[i])} ctx={lines[i][max(0,pos-60):pos+60]!r}")
