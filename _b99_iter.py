# -*- coding: utf-8 -*-
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
data = open(path, encoding="utf-8").read()
lines = data.splitlines()
# find "## Iteration log" line index
try:
    il_idx = next(i for i, ln in enumerate(lines) if ln.strip() == "## Iteration log")
except StopIteration:
    print("ERROR: no Iteration log"); raise SystemExit(1)
print("Iteration log at line", il_idx+1)
# The first entry after it is the newest. Show next 2 lines for sanity.
print("prev top entry:", lines[il_idx+1][:120])
print("second:", lines[il_idx+2][:80])