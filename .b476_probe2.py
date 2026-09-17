import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
c = io.open(path, encoding="utf-8").read()
m = "| K-Z3 | worker |"
s = c.find(m)
for needle in ["| K-Q2 |", "| K-W1 |", "| K-Z2 |", "※ falsify 2026-09-03", "\n## Iteration log"]:
    p = c.find(needle, s)
    print(needle, "->", p)
il = c.find("\n## Iteration log", s)
print("iter_log at", il)
print("--- 120 chars before iter_log ---")
print(repr(c[il - 120:il]))