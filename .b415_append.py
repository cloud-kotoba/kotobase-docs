#!/usr/bin/env python3
ev = open('/tmp/f_ev415c.txt', encoding='utf-8').read().rstrip('\n')
il = open('/tmp/f_il415c.txt', encoding='utf-8').read().rstrip('\n')
path = 'query-cosientist.md'
text = open(path, encoding='utf-8').read()
seg = '\n## Iteration log\n'
hdr = '## Iteration log\n'
p = text.find(seg)
if p < 0 or text.count(seg) != 1:
    raise SystemExit('anchor not unique: %d' % text.count(seg))
head_end = p + 1
after_hdr = p + 1 + len(hdr)
new = text[:head_end] + ev + '\n' + hdr + il + '\n' + text[after_hdr:]
open(path,'w',encoding='utf-8').write(new)
print('done ev+ilog inserted')
print('len', len(new))