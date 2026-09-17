import io, re
path = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
src = io.open(path, encoding="utf-8").read()
lines = src.split("\n")
out = []
for i, ln in enumerate(lines, 1):
    if "search.kotobase.net" in ln:
        idx = ln.find("search.kotobase.net")
        out.append("L%d: ...%s..." % (i, ln[max(0,idx-200):idx+300]))
io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench36_count_out.txt","w").write("\n\n".join(out)+"\n")
