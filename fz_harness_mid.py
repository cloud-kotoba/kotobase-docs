#!/usr/bin/env python3
src = open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/control-plane/authn/scripts/live_biscuit_query_bench.mjs").read()
lines = src.splitlines()
for i in range(80, 220):
    print(f"{i+1}: {lines[i][:180]}")
print("<<END>>")
