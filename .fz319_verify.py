import io
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s = open(p, encoding="utf-8").read()
lines = s.split("\n")
print("TOTAL", len(lines))
print("run319A cold 3/20 count:", s.count("run319A cold 3/20"))
print("falsify \u7b2c147\u56de occurrence:", s.count("\u7b2c147\u56de"))
# iter-log entry present once?
il_target = "falsify \u7b2c147\u56de\u300206:39 JST"
print("iter target count:", s.count(il_target))
# K-Z3 row still one line (no split), row line index 278 contains our EV
print("L278 starts:", lines[278][:12])
print("EV in L278:", "run319A cold 3/20" in lines[278])
print("iterlog header idx:")
H = None
for i,l in enumerate(lines):
    if l.strip()=="## Iteration log": H=i; break
print("H=",H)
print("H+1 :", lines[H+1][:50])
print("H+2 :", lines[H+2][:50])