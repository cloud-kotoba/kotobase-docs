import math
f=open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md')
lines=f.readlines()
print('TOTAL_LINES', len(lines))
print('L208_TAIL', repr(lines[207][-700:]))
print('LAST_LINE', repr(lines[-1][:160]))
