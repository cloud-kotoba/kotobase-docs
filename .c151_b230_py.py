import io
s = io.open('query-cosientist.md', encoding='utf-8', newline='').read().split('\n')
o = io.open('.c151_b230.txt', 'w', encoding='utf-8')
found = False
for i, l in enumerate(s):
    if 'bench  第230回' in l or 'bench 第230回' in l:
        o.write("line %d: %s\n" % (i, l[:900]))
        found = True
        break
if not found:
    o.write("bench 第230回 NOT FOUND\n")
o.close()