import re, sys

p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = open(p, encoding="utf-8").read()
lines = s.splitlines()
print("TOTAL_LINES", len(lines))
print("CHARS", len(s))

# Find K-Z3 hypothesis row(s)
for i, ln in enumerate(lines):
    if "K-Z3" in ln and ("|" in ln):
        print("KZ3ROW line", i + 1, ":", ln[:600])

print("---- last 12 lines ----")
for i, ln in enumerate(lines[-12:], start=len(lines) - 11):
    print(i, ":", ln[:700])
