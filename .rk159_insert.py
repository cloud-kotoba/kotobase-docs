#!/usr/bin/env python3
import io, sys

path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
entry_path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.rk159_entry.txt"

with io.open(path, "r", encoding="utf-8") as f:
    text = f.read()

with io.open(entry_path, "r", encoding="utf-8") as f:
    entry = f.read().rstrip("\n")

header = "## Iteration log\n"
anchor = header + "- 2026-09-07: bench 第161回。16:09 JST tick。HEAD 4661225 = bench 第160回"

if text.count(anchor) != 1:
    print("ANCHOR_COUNT=%d (expected 1)" % text.count(anchor))
    sys.exit(1)

new_text = text.replace(anchor, header + entry + "\n" + anchor[len(header):], 1)

with io.open(path, "w", encoding="utf-8") as f:
    f.write(new_text)

# verify
with io.open(path, "r", encoding="utf-8") as f:
    v = f.read()
print("HDR_COUNT=%d" % v.count("## Iteration log"))
print("RANK159_PRESENT=%s" % ("rank 第159回" in v))
i159 = v.find("rank 第159回")
i161 = v.find("bench 第161回")
print("ORDER_159_BEFORE_161=%s" % (i159 != -1 and i161 != -1 and i159 < i161))