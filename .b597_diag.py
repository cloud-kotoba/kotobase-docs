#!/usr/bin/env python3
DOC = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with open(DOC) as f:
    lines = f.read().split("\n")
out = []
for i, l in enumerate(lines):
    if "| K-Z3 |" in l:
        out.append(f"line {i+1}: starts_with_piped={l.startswith('| K-Z3 |')} len={len(l)} head={l[:40]!r} tail={l[-30:]!r}")
with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b597_diag2.txt", "w") as f:
    f.write("\n".join(out) + "\n")
