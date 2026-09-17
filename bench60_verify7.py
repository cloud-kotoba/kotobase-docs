import io
src = io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md", encoding="utf-8").read()
lines = src.split("\n")
idx = [i for i, ln in enumerate(lines) if ln.startswith("| K-Z3 | worker |")]
out = ["KZ3 rows: %s, run174A in row: %s" % (idx, "run174A" in lines[idx[0]]),
       "row tail: %r" % lines[idx[0]][-350:],
       "log line1718 head: %r" % lines[1717][:120] if len(lines) > 1717 else "log missing",
       "total lines: %d" % len(lines)]
io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench60_verify7.txt", "w", encoding="utf-8").write("\n".join(out))
