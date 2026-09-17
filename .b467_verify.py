#!/usr/bin/env python3
import io
ls = io.open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md', encoding='utf-8').readlines()
print("total lines:", len(ls))
print("L403 tail:", repr(ls[402][-240:]))
print("L404:", repr(ls[403][:40]))
print("L405 head:", repr(ls[404][:120]))
print("L406 head:", repr(ls[405][:80]))