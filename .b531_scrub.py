import unicodedata
p = '.b531_runner.sh'
s = open(p, encoding='utf-8').read()
keep = []
for ch in s:
    if unicodedata.combining(ch):
        continue
    keep.append(ch)
clean = ''.join(keep)
open(p, 'w', encoding='utf-8').write(clean)
removed = len(s) - len(clean)
print('removed', removed, 'len', len(clean))