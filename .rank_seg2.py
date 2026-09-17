s=open('query-cosientist.md',encoding='utf-8').read()
j=s.find('run378')
if j>=0:
    open('/tmp/rank_seg2.txt','w',encoding='utf-8').write(s[j:j+4500])
else:
    open('/tmp/rank_seg2.txt','w',encoding='utf-8').write('notfound')