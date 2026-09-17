#!/usr/bin/env python3
src = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/control-plane/authn/scripts/live_biscuit_query_bench.mjs").read()
lines = src.splitlines()
print("total lines:", len(lines))
# print first 80 lines
for i in range(0, min(80, len(lines))):
    print(f"{i+1}: {lines[i][:180]}")
print("<<END>>")
