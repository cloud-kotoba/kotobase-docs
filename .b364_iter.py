import io
with io.open("query-cosientist.md", "r", encoding="utf-8") as f:
    c = f.read()
lines = c.split("\n")
ih = [i for i, ln in enumerate(lines) if ln.strip() == "## Iteration log"]
outs = ["header idx: %s" % ih]
if ih:
    h = ih[0]
    # print entries after header until a blank
    for j in range(h+1, min(h+12, len(lines))):
        outs.append("[%d] %r" % (j, lines[j][:140]))
outs.append("has '第158回' count: %d" % c.count("第158回"))
outs.append("has '第157回' count: %d" % c.count("第157回"))
with io.open("/tmp/iter_head.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(outs))
print("ok")