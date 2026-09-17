p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
lines = open(p, encoding="utf-8").read().split("\n")
n = len(lines)
print("TOTAL", n)
H = None
for i,l in enumerate(lines):
    if l.strip()=="## Iteration log":
        H=i; break
print("H(0based)=", H, "1based line", H+1)
print("line before H (1based)", H, ":", repr(lines[H-1][:60]))
print("H+1:", repr(lines[H+1][:120]))
print("H+2:", repr(lines[H+2][:120]))
print("H+3:", repr(lines[H+3][:120]))
print("H+4:", repr(lines[H+4][:120]))
# last K-Z3 evidence line = H-1. Show its tail.
print("K-Z3 cell last line tail:", lines[H-1][-300:])
# confirm K-Z3 hypothesis row start
for i in range(0, H):
    if lines[i].startswith("| K-Z3 |"):
        print("KZ3 row 0based", i, "1based", i+1, "LEN", len(lines[i]))
        break