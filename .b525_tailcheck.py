f=open('query-cosientist.md','r',encoding='utf-8').read().splitlines(1)
line=f[278]
print('LEN',len(line))
print('LINE_IS_279', line[:6].replace('|','PIPE'))
print('COUNT_run525', line.count('run525'))
print('TAIL>>>'+line[-180:]+'<<<')