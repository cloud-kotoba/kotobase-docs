import io
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
with io.open(p,encoding="utf-8" as f:
    lines=f.readlines()
l=lines[278]
out=l[-1200:]
with io.open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b380_tail.txt","w",encoding="utf-8") as g:
    g.write("LINELEN=%d\n"%len(l))
    g.write("TAIL>\n")
    g.write(out)
    g.write("\n<EOF\n")