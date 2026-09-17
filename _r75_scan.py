import io
p = 'query-cosientist.md'
data = open(p, 'rb').read().decode('utf-8', errors='replace')
out = []
# last occurrence of run195 (falsify run195 evidence)
i = data.rfind('run195')
out.append('run195@%d' % i)
if i >= 0:
    out.append(data[i-200:i+900])
j = data.rfind('NEXT:')
out.append('NEXT@%d' % j)
if j >= 0:
    out.append(data[j-300:j+300])
open('_r75_tail.txt', 'w').write('\n---\n'.join(out))
