import re, sys
out = open('.c151_l279.txt', 'w', encoding='utf-8')
s = open('query-cosientist.md', encoding='utf-8').read().split('\n')
l = s[278]
out.write("line279 length: %d\n" % len(l))
for kw in ['run518', 'run517', 'run516']:
    fm = None
    for m in re.finditer(re.escape(kw), l):
        if m.start() > 5:  # near-start match is the hypothesis body, skip; want evidence-cell occurrences
            fm = m
    if fm is not None:
        a = max(0, fm.start() - 180)
        b = min(len(l), fm.end() + 60)
        out.write("--- %s @ %d ---\n" % (kw, fm.start()))
        out.write(l[a:b] + "\n")
out.write("=== last 600 chars of line 279 ===\n")
out.write(l[-600:] + "\n")
out.close()