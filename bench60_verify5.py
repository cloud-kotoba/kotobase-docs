import io
src = io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md", encoding="utf-8").read()
lines = src.split("\n")
idx = [i for i, ln in enumerate(lines) if ln.startswith("| K-Z3 | worker |")]
out = ["K-Z3 rows: %s" % idx]
for i in idx:
    out.append("line %d tail: %r" % (i + 1, lines[i][-400:]))
out.append("run174 total: %d, in KZ3 row: %s" % (src.count("run174"), any("run174A" in lines[i] for i in idx)))
io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench60_verify5.txt", "w", encoding="utf-8").write("\n".join(out))
