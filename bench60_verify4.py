import io
src = io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md", encoding="utf-8").read()
out = []
out.append("run174 count: %d" % src.count("run174"))
lines = src.split("\n")
l207 = lines[206]
out.append("line207 len=%d tail=%r" % (len(l207), l207[-300:]))
out.append("log tail: %r" % (lines[-1][-200:],))
io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench60_verify4.txt", "w", encoding="utf-8").write("\n".join(out))
print("ok")
