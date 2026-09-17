#!/usr/bin/env python3
import io
path = "query-cosientist.md"
with io.open(path, "r", encoding="utf-8") as f:
    content = f.read()
header = "## Iteration log"
idx = content.index(header)
after = content[idx+len(header): idx+len(header)+80]
print(repr(after))
print("header_count=", content.count("## Iteration log"))