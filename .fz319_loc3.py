p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().split("\n")
H = None
for i,l in enumerate(lines):
    if l.strip()=="## Iteration log":
        H=i; break
print("TOTAL", len(lines), "H=", H)
print("before H:", repr(lines[H-1][:50]))
print("H+1 :", repr(lines[H+1][:130]))
print("H+2 :", repr(lines[H+2][:130]))
# current NEXT present in iter-log top?
for k in [H+1,H+2,H+3]:
    if "NEXT" in lines[k]:
        print("NEXT-line idx", k, ":", lines[k][:180])
# is run319 already in K-Z3 evidence cell lines above H?
cnt=0
for i in range(H-5,H):
    if "run319" in lines[i]:
        cnt+=1; print("cell run319 at", i, ":", lines[i][:60])
print("run319 in last 5 cell lines:", cnt)