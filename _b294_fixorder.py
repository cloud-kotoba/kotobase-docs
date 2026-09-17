#!/usr/bin/env python3
import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()

H = None
for i, ln in enumerate(lines):
    if ln.rstrip("\n") == "## Iteration log":
        H = i
        break
assert H is not None

# The bench entry line is currently just above the header: H-1.
assert lines[H-1].startswith("- 2026-09-07: bench 第121回"), repr(lines[H-1][:60])
# Optionally a blank line directly above bench entry (H-2 blank).
entry = lines.pop(H-1)   # remove bench entry (header shifts down to H-1)
H2 = H - 1               # header now at this index
lines.insert(H2 + 1, entry)  # put bench entry right after header
with io.open(p, "w", encoding="utf-8") as f:
    f.writelines(lines)
print("fixed order; now header at line", H2+1, "bench entry at", H2+2)