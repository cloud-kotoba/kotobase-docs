#!/usr/bin/env python3
import io

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    data = f.read()

# Current file lost its '## Iteration log' header (my earlier insert consumed it).
# Re-insert header exactly once before the first '-' entry line in the file.
needle = "- 2026-09-08: rank 第187回"
i = data.find(needle)
assert i != -1, "rank entry not found"
# Ensure no duplicate header
print("header count before fix:", data.count("## Iteration log"))
# The rank entry should be the first entry; prefix with header.
# Find end of preceding content (anything before position i). Insert header right at i.
data = data[:i] + "## Iteration log\n" + data[i:]

with io.open(path, "w", encoding="utf-8") as f:
    f.write(data)

with io.open(path, "r", encoding="utf-8") as f:
    out = f.read()
print("header count after fix:", out.count("## Iteration log"))
print("entry count:", out.count("rank 第187回"))
lines = out.split("\n")
print("line0:", lines[0][:40])
print("line1:", lines[1][:40])
print("line2:", lines[2][:40])