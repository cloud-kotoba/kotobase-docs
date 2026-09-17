# -*- coding: utf-8 -*-
import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(p, encoding="utf-8") as f:
    lines = f.readlines()
line = lines[239]
idx = line.find("run236A")
tail = line[idx-4:]
out = "/tmp/rank_r236_tail.txt"
with io.open(out, "w", encoding="utf-8") as f:
    f.write(tail)
    f.write("\n\nLEN_TAIL=" + str(len(tail)) + "\n")
print("ok")