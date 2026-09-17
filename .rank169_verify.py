#!/usr/bin/env python3
import io, re
MD = "query-cosientist.md"
txt = io.open(MD, "r", encoding="utf-8").read()
print("hdr_count =", txt.count("\n## Iteration log\n") + (1 if txt.startswith("## Iteration log\n") else 0))
print("rank169_count =", txt.count("rank 第169回。21:08"))
print("rank168_after =", txt.split("## Iteration log\n",1)[1].count("rank 第168回。20:39"))
# order of first 3 entries
idx = txt.index("## Iteration log\n")
seg = txt[idx:idx+500]
lines = [l for l in txt[idx:].splitlines() if l.startswith("- 2026-09-07")][:3]
for l in lines:
    print("ENTRY:", l[:70])