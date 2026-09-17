import re
def nr_p50(xs):
    s=sorted(xs); n=len(s); r=min(n,(n*50+99)//100); return s[r-1]
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_fz291_out.txt"
blocks={}; cur=None
for line in open(p):
    line=line.rstrip("\n")
    if line.startswith("=== run"):
        cur=line.split()[1]; blocks[cur]=[]
    elif line.startswith("=== landing"):
        cur="control"; blocks[cur]=[]
    elif re.match(r"^\d{3} ",line):
        code,t=line.split(); blocks[cur].append(float(t))
for k,v in blocks.items():
    cold=sum(1 for x in v if x>=0.5)
    print(f"{k}: n={len(v)} cold>=0.5s={cold} p50(nr)={nr_p50(v):.4f} min={min(v):.4f} max={max(v):.4f}")