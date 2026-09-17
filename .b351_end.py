#!/usr/bin/env python3
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines=open(p,encoding='utf-8').read().split('\n')
l=lines[278]
print("LEN:", len(l))
print("RAW TAIL 300:", repr(l[-300:]))
print()
print("run352 count:", sum(1 for x in lines if 'run352' in x))
print("run351 count:", sum(1 for x in lines if 'run351' in x))
# find index of tail marker to anchor insertion
idx=l.find('status 判定は rank に委ねる (rank 専門)。')
print("tail-marker idx:", idx)
print("context around marker:", repr(l[idx-40:idx+20]))