lines=open('query-cosientist.md',encoding='utf-8').read().split('\n')
l=lines[278]
print('L279_LEN',len(l))
print('TAIL300',repr(l[-300:]))
# check for replacement chars
import re
bad=re.findall(r'[\ufffd]', l)
print('REPLACEMENT_CHARS', len(bad))