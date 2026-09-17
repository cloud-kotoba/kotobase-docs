p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
lines=open(p).readlines()
hits=[(i+1, l[:70]) for i,l in enumerate(lines) if 'bench 第8' in l[:40] or ('第8' in l[:30] and 'bench' in l[:30])]
for h in hits[:20]:
    print(h)
# also show what lines 200-215 of iteration log area look like (search 'bench 第' prefix lines)
pref=[(i+1,l[:60]) for i,l in enumerate(lines) if l.startswith('- 2026-09-06: bench')]
for h in pref[-6:]:
    print('PREF', h)
