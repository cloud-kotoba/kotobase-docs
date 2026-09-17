p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().split("\n")
print("TOTAL", len(lines))
H=None
for i,l in enumerate(lines):
    if l.strip()=="## Iteration log":
        H=i; break
print("H=",H)
print("H+1:", lines[H+1][:90])
print("H+2:", lines[H+2][:90])
print("L278 K-Z3 row LEN", len(lines[278]))
print("L278 END 300:", lines[278][-300:])
# does L278 already reference my run319 (independent)? count
print("run319 in L278:", lines[278].count("run319"))
print("bench 第133回 in L278:", lines[278].count("bench 第133回"))
print("rank 第141回 in L278:", lines[278].count("rank 第141回"))