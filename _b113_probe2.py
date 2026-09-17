#!/usr/bin/env python3
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
src = open(path, encoding="utf-8").read()
i = src.find("第112回, K-Z3 1時台")
# find end of this line (next \n\n or next "\nbench ")
j = src.find("\n", i)
seg = src[i:j]
print("LEN run276 line:", len(seg))
print("END 120 chars:")
print(seg[-120:])
# find "bench 2026-09-07 (第110回"
k = src.find("bench 2026-09-07 (第110回, K-Z3 24時台")
print("\nrun272 idx:", k)
print("between run276 end and run272:", repr(src[j:j+40]))