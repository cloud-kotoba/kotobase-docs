import io

p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(p, "r", encoding="utf-8") as f:
    lines = f.readlines()

out = []
# iter-log entries start after line 406 (index 405). print lines 406..410 (1-indexed)
for i in range(405, min(412, len(lines))):
    ln = lines[i].rstrip("\n")
    out.append("L%d: %s" % (i+1, ln[:900]))
    out.append("" if not ln else "  ...len=%d" % len(ln))

with io.open("/tmp/bench_ilog_hdr.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(out))