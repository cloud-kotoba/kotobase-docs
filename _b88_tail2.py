p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
lines=open(p).readlines()
# show tail lines to find where iteration log ends / what latest entries are
for i,l in enumerate(lines[-30:]):
    print(len(lines)-30+i+1, l[:80])
