import io
with io.open("query-cosientist.md", "r", encoding="utf-8") as f:
    c = f.read()
# L279 line: find line containing "| K-Z3 |"
lines = c.split("\n")
lk = [i for i, ln in enumerate(lines) if "| K-Z3 | worker |" in ln]
outs = ["K-Z3 line idx: %s" % lk]
for i in lk:
    outs.append("len=%d tail150=...%s" % (len(lines[i]), lines[i][-150:]))
# find iterlog header
ih = [i for i, ln in enumerate(lines) if ln.strip() == "## Iteration log"]
outs.append("iterlog header idx: %s" % ih)
for i in ih:
    outs.append("+1: %r" % lines[i+1][:90])
# count run365/run364 in whole doc
outs.append("run364 count: %d, run365 count: %d" % (c.count("run364"), c.count("run365")))
with io.open("/tmp/state2.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(outs))
print("ok")