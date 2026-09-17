import io, sys
md_path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open("/tmp/b430_ev.txt", encoding="utf-8") as fh:
    ev = fh.read()
with io.open("/tmp/b430_il.txt", encoding="utf-8") as fh:
    il = fh.read()
with io.open(md_path, encoding="utf-8") as fh:
    md = fh.read()
hdr = "## Iteration log"
i = md.rfind(hdr
md2 = md[:i] + "\n" + ev + "\n\n" + md[i:]
h2 = md2.rfind(hdr
nl = md2.find("\n", h2
md3 = md2[:nl+1] + il + "\n\n" + md2[nl+1:]
with io.open(md_path, "w", encoding="utf-8") as fh:
    fh.write(md3
print("append ok len %d" % len(md3)
