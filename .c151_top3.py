import io
s = io.open('query-cosientist.md', encoding='utf-8', newline='').read().split('\n')
o = io.open('.c151_top3.txt', 'w', encoding='utf-8')
# find iter-log header
for i, l in enumerate(s):
    if l.strip() == '## Iteration log':
        for j in range(i+1, min(i+4, len(s))):
            o.write("L%s: %s\n" % (j+1, s[j][:140]))
        o.write("(total lines %d)\n" % len(s))
        break
o.close()