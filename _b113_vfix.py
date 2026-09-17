#!/usr/bin/env python3
import sys
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
src = open(path, encoding="utf-8").read()
i = src.find("委ねる (rank 専門)。\nbench 2026-09-07 (第110回, K-Z3 24時台(0時台) n 積み増し run272A–C")
j = src.find("委ねる (rank 専門)")
print("has clean newline before run272:", i != -1)
print("boundary repr:", repr(src[j:j+140]))