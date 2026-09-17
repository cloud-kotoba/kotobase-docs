import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as fh:
    t = fh.read()

for pat in ["run642A-C", "21/60 (35.0%)", "falsify \u7b2c158\u56de", "falsify 2026-09-16 (\u7b2c158\u56de"]:
    print(pat, "->", t.count(pat))

lines = t.split("\n")
hits = [i for i, ln in enumerate(lines) if "run642A-C" in ln]
print("lines_with_run642:", hits)
for i in hits:
    print(f"L{i+1} len={len(lines[i])} head={lines[i][:80]!r}")
