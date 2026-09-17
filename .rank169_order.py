#!/usr/bin/env python3
import io
MD = "query-cosientist.md"
txt = io.open(MD, "r", encoding="utf-8").read()
idx = txt.index("## Iteration log\n")
lines = [l for l in txt[idx:].splitlines() if l.startswith("- 2026-09-07")]
print("total iter entries:", len(lines))
for i, l in enumerate(lines[:8]):
    # extract tick type + time
    print(i, "|", l[:60])
# grep exact bench177 title
print("bench177 title present:", any(l.startswith("- 2026-09-07: bench 第177回") for l in lines))