import io
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
d=io.open(p,encoding="utf-8").read()
h=d.find("## Iteration log")
print("hdr at",h)
seg=d[h:h+900]
print(seg.replace("\n"," ||\n")[:1600])