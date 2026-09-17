#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import io
PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(PATH, "r", encoding="utf-8") as f:
    lines = f.read().split("\n")
kz = None
for i, line in enumerate(lines):
    if line.startswith("| K-Z3 | worker | K-Z1/K-Z2"):
        kz = i; break
print("KZ3 line idx", kz, "len", len(lines[kz]))
print("TAIL>>>", lines[kz][-450:])