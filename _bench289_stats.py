import re, statistics as st
p="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/_bench_run289_out.txt"
blocks={}
cur=None
for line in open(p):
    line=line.rstrip("\n")
    if line.startswith("=== run"):
        cur=line.split()[1]
        blocks[cur]=[]
    elif line.startswith("=== landing"):
        cur="control"
        blocks[cur]=[]
    elif re.match(r"^\d{3} ",line):
        code,t=line.split()
        blocks[cur].append(float(t))
def nearest_rank_p50(xs):
    s=sorted(xs)
    return s[min(len(s)-1,(len(s)*50)//100)]  # ceil(n*0.5)-1 index... nearest-rank: rank=ceil(p*n)=ceil(20*0.5)=10 -> idx 9
def nr_p50(xs):
    s=sorted(xs); n=len(s); r=max(1,round(n*50/100+0.0001)); r=min(n,(n*50+99)//100); return s[r-1]
for k,v in blocks.items():
    cold=sum(1 for x in v if x>=0.5)
    print(f"{k}: n={len(v)} cold>=0.5s={cold} p50(nr)={nr_p50(v):.4f} min={min(v):.4f} max={max(v):.4f}")