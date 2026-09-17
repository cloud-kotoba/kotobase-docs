import io
# scrub known corruption chars injected during tool-call transmission
BADS=['\u6050','\u025c','\u58f2','\u200b','\u200c','\u200d']
FN='.b411_insert.py'
s=open(FN,'rb').read().decode('utf-8')
for ch in BADS:
    s=s.replace(ch, '')
open(FN,'w',encoding='utf-8').write(s)
print('scrubbed', len(BADS))