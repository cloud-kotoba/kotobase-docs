#!/usr/bin/env python3
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
src = open(path, encoding="utf-8").read()
i = src.find("第126回, K-Z3 1時台 n 積み増し run277A–C")
j = src.find("\n", i)
print("falsify126 len:", j-i)
print("after falsify126 line ->", repr(src[j:j+60]))