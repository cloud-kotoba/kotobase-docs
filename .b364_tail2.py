import io
with io.open("query-cosientist.md", "r", encoding="utf-8") as f:
    lines = f.readlines()
l279 = lines[278]
outs = ["tail120: " + repr(l279[-120:])]
outs.append("line364head: " + repr(lines[363][:80]))
with io.open("/tmp/anchor2.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(outs))
print("ok")