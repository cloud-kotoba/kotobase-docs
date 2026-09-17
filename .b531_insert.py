import unicodedata

def clean(s):
    out = []
    for ch in s:
        o = ord(ch)
        if 0x300 <= o and o <= 0x36F:
            continue
        if 0x200B <= o and o <= 0x200D:
            continue
        out.append(ch)
    return ''.join(out)

def rd(p):
    data = open(p, encoding='utf-8').read()
    return clean(data.strip())

ev = rd('.b531_ev.txt')
iter_t = rd('.b531_iter.txt')

path = 'query-cosientist.md'
s = open(path, encoding='utf-8').read()
lines = s.split('\n')
lines[278] = lines[278] + ' ' + ev
s2 = '\n'.join(lines)
marker = '## Iteration log'
assert marker in s2
idx = s2.index(marker)
pos = idx + len(marker)
s2 = s2[:pos] + '\n' + iter_t + s2[pos:]
open(path, 'w', encoding='utf-8').write(s2)
print('done', len(ev), len(iter_t))