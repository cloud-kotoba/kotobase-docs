import io
with io.open("query-cosientist.md", "r", encoding="utf-8") as f:
    c = f.read()
outs = []
outs.append("run364 evid: %d" % c.count("run364A cold 0/20"))
outs.append("bench158 iter: %d" % c.count("bench 第158回。15:12"))
outs.append("run365 evid: %d" % c.count("run365A"))
outs.append("falsify 167 iter: %d" % c.count("falsify 第167回"))
lines = c.split("\n")
ih = [i for i, ln in enumerate(lines) if ln.strip() == "## Iteration log"]
outs.append("iterlog header idx: %s" % ih)
if ih:
    outs.append("+1: %r" % lines[ih[0]+1][:80])
    outs.append("+2: %r" % lines[ih[0]+2][:80])
with io.open("/tmp/verify_committed.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(outs))
print("ok")