import sys
out = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/rank38_out6.txt','w')
sys.stdout = out
import os, re
os.chdir('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs')
p = 'query-cosientist.md'
txt = open(p).read()
print('run106 count:', txt.count('run106'))
print('run107 count:', txt.count('run107'))
print('run105 count:', txt.count('run105'))
print('file size:', len(txt))
out.close()
