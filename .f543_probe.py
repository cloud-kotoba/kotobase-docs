#!/usr/bin/env python3
import sys
path="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(path,encoding='utf-8').read().split('\n')
print("total_lines=%d" % len(lines))
l279=lines[278]  # 0-indexed -> line 279
print("L279_START:%s" % l279[:60].replace('\t',' '))
print("L279_TAIL160:%s" % l279[-160:])
l414=lines[413]
print("L414_START100:%s" % l414[:100])
# find NEXT in l414
i=l414.find('NEXT')
print("L414_NEXT_CTX:%s" % l414[i:i+220] if i>=0 else "no NEXT")
l415=lines[414]
print("L415_START80:%s" % l415[:80])