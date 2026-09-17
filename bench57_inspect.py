D='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs'
lines=open(D+'/query-cosientist.md').read().split('\n')
l=lines[205].rstrip()
print('len:',len(l))
print('last60:',repr(l[-60:]))
print('first60:',repr(l[:60]))
