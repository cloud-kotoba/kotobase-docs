p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().split("\n")
H = None
for i,l in enumerate(lines):
    if l.strip()=="## Iteration log":
        H=i; break
print("TOTAL", len(lines), "H=", H)
print("before H:", repr(lines[H-1][:50]))
print("H+1:", repr(lines[H+1][:100]))
print("H+2:", repr(lines[H+2][:100]))
# run319 already present anywhere?
for i,l in enumerate(lines):
    if "run319" in l:
        print("run319 at", i, ":", l[:60])
# K-Z3 evidence cell: does rank141 fold sit in cell as new line above H? print last 3 lines before H
for k in range(3,0,-1):
    print("preH-",k, len(lines[H-k]), ":", repr(lines[H-k][:70]))