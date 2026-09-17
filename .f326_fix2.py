#!/usr/bin/env python3
import io
PATH="query-cosientist.md"
lines=io.open(PATH,encoding="utf-8").readlines()
row=lines[278]
i=row.find("第151回")
assert i>0
seg=row[i:]
n=seg.count("渫")
seg_fixed=seg.replace("渫","測")
print("渫 in my segment before:", n)
lines[278]=row[:i]+seg_fixed
io.open(PATH,"w",encoding="utf-8").write("".join(lines))
# verify
lines2=io.open(PATH,encoding="utf-8").readlines()
seg2=lines2[278][lines2[278].find("第151回"):]
print("渫 in my segment after:", seg2.count("渫"))