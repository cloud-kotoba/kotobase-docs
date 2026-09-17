import statistics
def parse(fn):
    vals=[]
    with open(fn) as f:
        for ln in f:
            p=ln.split()
            if len(p)>=2:
                try:
                    vals.append(float(p[1]))
                except ValueError:
                    pass
    return vals
def nearest_rank_p50(v):
    s=sorted(v)
    n=len(s)
    return s[(n-1)//2] if n else None
def stats(name, fn):
    v=parse(fn)
    cold=[x for x in v if x>=0.5]
    vv=[x for x in v if x<0.5]
    p50=nearest_rank_p50(v)
    w50=nearest_rank_p50(vv) if vv else None
    print("%s n=%d cold>=0.5s=%d p50=%.4f warm_p50=%s max=%.4f"%(name,len(v),len(cold),p50,"%.4f"%w50 if w50 else None,max(v)))
base="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/"
stats("A",base+".f397_397A.txt")
stats("B",base+".f397_397B.txt")
stats("C",base+".f397_397C.txt")
stats("land",base+".f397_397land.txt")
print("COLD_A",[x for x in parse(base+".f397_397A.txt") if x>=0.5])
print("COLD_B",[x for x in parse(base+".f397_397B.txt") if x>=0.5])