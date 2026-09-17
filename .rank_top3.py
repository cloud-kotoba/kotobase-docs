s=open('query-cosientist.md',encoding='utf-8').read()
i=s.find('## Iteration log')
open('/tmp/rank_top3.txt','w',encoding='utf-8').write(s[i:i+3600])