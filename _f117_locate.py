p='/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md'
lines=open(p,encoding='utf-8').readlines()
out=[]
for i,ln in enumerate(lines):
    if '| K-Z3 |' in ln:
        out.append((i, repr(ln[-200:])))
        # print short evidence tail too
with open('/tmp/kz3_loc.txt','w',encoding='utf-8') as f:
    f.write("rows with | K-Z3 |:\n")
    for i,t in out:
        f.write("idx=%d len=%d tail=%r\n" % (i, len(lines[i]), t))
    f.write("total lines=%d\n" % len(lines))
    # also find latest run25x occurrence
    import re
    for pat in ['run25[0-9]','run255','run256','run254']:
        hits=[i for i,l in enumerate(lines) if re.search(pat,l)]
        f.write("pattern %s hits=%d last=%s\n" % (pat, len(hits), hits[-5:] if hits else None))
print("done")