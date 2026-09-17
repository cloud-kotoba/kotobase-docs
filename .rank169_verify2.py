#!/usr/bin/env python3
import io
MD = "query-cosientist.md"
txt = io.open(MD, "r", encoding="utf-8").read()
idx = txt.index("## Iteration log\n")
hdrcount = txt.count("\n## Iteration log\n") + (1 if txt.startswith("## Iteration log\n") else 0)
print("hdr_count =", hdrcount)
lines = [l for l in txt[idx:].splitlines() if l.startswith("- 2026-09-07")]
print("total entries:", len(lines))
for i, l in enumerate(lines[:6]):
    print(i, "|", l[:52])