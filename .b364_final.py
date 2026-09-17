import io
with io.open("query-cosientist.md", "r", encoding="utf-8") as f:
    c = f.read()
lines = c.split("\n")
outs = []
outs.append("has run364 evidence: %d" % c.count("run364A cold 0/20"))
outs.append("has run365 evidence: %d" % c.count("run365A"))
outs.append("has bench 第158回 iter: %d" % c.count("bench 第158回。15:12"))
lk = [i for i, ln in enumerate(lines) if "| K-Z3 | worker |" in ln]
outs.append("K-Z3 line idx: %s len=%d" % (lk, len(lines[lk[0]]) if lk else -1))
if lk:
    outs.append("tail160: " + lines[lk[0]][-160:])
ih = [i for i, ln in enumerate(lines) if ln.strip() == "## Iteration log"]
outs.append("iterlog header idx: %s" % ih)
if ih:
    outs.append("+1: " + lines[ih[0]+1][:100])
with io.open("/tmp/final_state.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(outs))
print("ok")