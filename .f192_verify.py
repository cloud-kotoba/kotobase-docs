#!/usr/bin/env python3
import io
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s=io.open(p,encoding="utf-8").read()
for pat in ["run434","falsify 第192回","第192回","u200b","u200c","u200d","#####"]:
    print(pat, s.count(pat))