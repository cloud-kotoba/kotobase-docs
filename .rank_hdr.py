#!/usr/bin/env python3
import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    txt = f.read()

# Update rank block header
old_hdr = "rank (期待 gain × 確率, 2026-09-06 第98回):"
new_hdr = "rank (期待 gain × 確率, 2026-09-06 第111回):"
hdr_cnt = txt.count(old_hdr)

out = ["hdr_count=%d" % hdr_cnt]
if hdr_cnt == 1:
    txt = txt.replace(old_hdr, new_hdr)
    out.append("HDR_UPDATED")

with io.open(path, "w", encoding="utf-8") as f:
    f.write(txt)
with io.open("/tmp/rank_hdr.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))