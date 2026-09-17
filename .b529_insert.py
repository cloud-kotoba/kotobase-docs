#!/usr/bin/env python3
import re
P='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
def stripc(s):
    return ''.join(ch for ch in s if not (0x0300 <= ord(ch) <= 0x036F))
ev = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b529_ev.txt',encoding='utf-8').read().strip()
iterl = open('/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b529_iter.txt',encoding='utf-8').read().strip()
ev = stripc(ev); iterl = stripc(iterl)
lines = open(P,encoding='utf-8').read().split('\n')
# locate K-Z3 hypothesis row
kz3 = next(i for i,ln in enumerate(lines) if re.match(r'^\s*\| K-Z3 \s*\|', ln))
lines[kz3] = lines[kz3].rstrip('\n') + ' ' + ev + '\n'
# locate iteration log header, insert new entry after it
ilog = next(i for i,ln in enumerate(lines) if ln.strip() == '## Iteration log')
# ensure header line has no trailing content issues
lines.insert(ilog+1, iterl)
out = '\n'.join(lines)
out = stripc(out)
open(P,'w',encoding='utf-8').write(out)
print('inserted. kz3_row=',kz3,'ilog_no=',ilog)
print('run529_count=', out.count('run529'))
print('comb_remaining=', sum(1 for c in out if 0x0300 <= ord(c) <= 0x036F))