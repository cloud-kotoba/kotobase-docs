lines=open('query-cosientist.md',encoding='utf-8').read().split('\n')
l=lines[278]
print('L279_LEN',len(l))
print('L279_LAST40',repr(l[-40:]))
print('L280_FIRST120',repr(lines[279][:120]))
print('L280_LEN',len(lines[279]))