import io
s = open('query-cosientist.md', encoding='utf-8').read()
lines = s.split('\n')
ln = lines[242]
open('/tmp/b100_tail2.txt','w',encoding='utf-8').write(
  'LEN:%d\nTAIL80:%r\nPIPECOUNT:%d\n' % (len(ln), ln[-80:], ln.count('|')))