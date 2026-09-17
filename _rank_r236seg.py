# -*- coding: utf-8 -*-
import io, sys
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(p, encoding="utf-8") as f:
    lines = f.readlines()
line = lines[239]  # line 240
idx = line.find("run236")
seg = line[idx-2: idx+900]
out = "/tmp/rank_r236_seg.txt"
with io.open(out, "w", encoding="utf-8") as f:
    f.write("FOUND_IDX=" + str(idx) + "\n")
    f.write(seg + "\n")
    f.write("\nLEN_LINE=" + str(len(line)) + "\n")
print("wrote", out)