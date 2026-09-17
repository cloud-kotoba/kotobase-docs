#!/usr/bin/env python3
import io
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=io.open(p,encoding="utf-8").read().split("\n")
# verify header at index 362 (line 363)
for idx in range(360, 367):
    print("PRE", idx+1, lines[idx][:90])