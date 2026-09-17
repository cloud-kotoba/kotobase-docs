#!/usr/bin/env python3
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(path, encoding='utf-8').read().split('\n')
for idx,l in enumerate(lines,1):
    n543 = l.count('run543')
    n241 = l.count('第241回')
    if n543 or n241:
        print("L%d run543=%d 第241=%d prefix=%s" % (idx, n543, n241, l[:30]))