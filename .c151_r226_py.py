import io, sys
out = io.open('.c151_r226_py.txt', 'w', encoding='utf-8')
s = io.open('query-cosientist.md', encoding='utf-8', newline='').read().split('\n')
found = False
for i, l in enumerate(s):
    if 'rank 第226回' in l:
        out.write("line %d: %s\n" % (i, l[:2500]))
        found = True
        break
if not found:
    out.write("rank 第226回 NOT FOUND in doc\n")
out.close()