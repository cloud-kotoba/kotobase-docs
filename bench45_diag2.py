import io
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
src = io.open(path, encoding="utf-8").read()
hrow = [ln for ln in src.split("\n") if ln.startswith("| K-Z3 | worker |")][0]
with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench45_diag2.txt", "w") as f:
    f.write("has 'run125A cold(>=0.5s) 1/20': %s\n" % str("run125A cold(>=0.5s) 1/20" in src))
    f.write("hrow contains run125A: %s\n" % str("run125A" in hrow))
    # what does the tail of hrow look like
    f.write("hrow tail: ...%s\n" % hrow[-300:])
    f.write("'run125A–C' anywhere: %d\n" % src.count("run125A–C"))
print("done")
