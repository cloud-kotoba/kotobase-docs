s=open('.b420_runner.sh','rb').read().decode('utf8')
bad=[]
for i,c in enumerate(s):
    o=ord(c)
    if (0x200b<=o<=0x200d) or (0x0300<=o<=0x036F) or (o==0xFEFF):
        bad.append((i,hex(o),c))
print('bad_count',len(bad))
import re
m=[i for i,c in enumerate(s) if c in '~\u0303']
print('tilde_pos',m[:6], [hex(ord(s[i]))) for i in m[:6]] if False else '')
print('has_comb_tilde',str('\u0303'）in s)