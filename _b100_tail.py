import io
lines = open('query-cosientist.md', encoding='utf-8').read().split('\n')
ln = lines[242]  # line 243
idx = ln.rfind('run247')
out = []
out.append('run247 last idx in line243: %d' % idx)
if idx >= 0:
    out.append('TAIL after idx: ' + repr(ln[idx:idx+120]))
    out.append('END: ' + repr(ln[-500:]))
else:
    # find last cold mention / last falsify 第112
    i2 = ln.rfind('第112回')
    out.append('第112回 idx: %d' % i2)
    out.append('END: ' + repr(ln[-500:]))
open('/tmp/b100_tail.txt', 'w', encoding='utf-8').write('\n'.join(out))