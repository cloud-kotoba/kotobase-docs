import io

p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()

out = []
out.append("total_lines=%d" % len(lines))
c497=0; c498=0; c_bench217=0
for ln in lines:
    c497 += ln.count("run497")
    c498 += ln.count("run498")
    c_bench217 += ln.count("bench 第217回")
out.append("run497_count=%d" % c497)
out.append("run498_count=%d" % c498)
out.append("bench217_count=%d" % c_bench217)

# iter log header line and first entry
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        out.append("iter_header=%d" % (i+1))
        # print first 2 entries after
        for j in range(i, min(i+2, len(lines))):
            l2 = lines[j].rstrip("\n")
            out.append("ITER_L%d %s" % (j+1, l2[:1600]))
        break

with io.open("/tmp/bench_probe498.txt","w",encoding="utf-8") as f:
    f.write("\n".join(out))