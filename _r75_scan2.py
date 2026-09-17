p = 'query-cosientist.md'
data = open(p, 'rb').read().decode('utf-8', errors='replace')
j = data.rfind('NEXT:')
# print tail of iteration log after the NEXT line, to see structure
open('_r75_logend.txt', 'w').write(data[j-2000:])
