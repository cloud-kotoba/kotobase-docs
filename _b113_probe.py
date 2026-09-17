#!/usr/bin/env python3
import sys
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
src = open(path, encoding="utf-8").read()
idx = src.find("第112回, K-Z3 1時台")
print("run276 idx:", idx)
print("--- around run276 boundary ---")
print(src[idx:idx+700])