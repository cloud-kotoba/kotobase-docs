import io
p="query-cosientist.md"
s=io.open(p,encoding="utf-8").read()
ev=io.open("/tmp/fal_ev420.txt",encoding="utf-8").read()
il=io.open("/tmp/fal_iter420.txt",encoding="utf-8").read()
for ch in ["\u200b","\u200c","\u200d","\ufeff"]:
    ev=ev.replace(ch,"")
    il=il.replace(ch,"")
lines=s.split("\n")
idx=None
for i,l in enumerate(lines):
    if l.startswith("| K-Z3 |"):
        idx=i
        break
assert idx is not None, "kz3 not found"
lines[idx]=lines[idx]+ev.rstrip("\n")
news="\n".join(lines)
anchor="## Iteration log\n"
ia=news.find(anchor)
assert ia!=-1,"anchor not found"
news = news[:ia+len(anchor)] + il.rstrip("\n") + "\n" + news[ia+len(anchor):]
io.open(p,"w",encoding="utf-8").write(news)
print("OK", news.count("run420"), news.count("run419"))