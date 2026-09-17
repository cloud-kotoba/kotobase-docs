import io
with io.open("query-cosientist.md", "r", encoding="utf-8") as f:
    lines = f.readlines()
# line 279 = index 278
l279 = lines[278]
outs = []
outs.append("L279 len=%d" % len(l279))
outs.append("L279 tail(400): ..." + l279[-400:])
# find iterlog header lines
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log" or ln.strip() == "## Iteration Log":
        outs.append("iterlog header at line %d" % (i + 1))
        if i + 1 < len(lines):
            outs.append("  +1: " + lines[i+1][:120])
        if i + 2 < len(lines):
            outs.append("  +2: " + lines[i+2][:80])
with io.open("/tmp/anchor279.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(outs))
print("ok")