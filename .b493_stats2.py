B="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b493"
def nearest_rank(vals, q):
    vals=sorted(vals)
    i=max(0, min(len(vals)-1, round(q*(len(vals)-1))))
    return vals[i]
out=[]
for lid in ["A","B","C","landing"]:
    vals=[float(x) for x in open(f"{B}_{lid}.ttfb") if x.strip()]
    cold=[v for v in vals if v>=0.5]
    out.append(f"{lid}: n={len(vals)} p50={nearest_rank(vals,0.5):.4f} p95={nearest_rank(vals,0.95):.4f} max={max(vals):.4f} cold={len(cold)}/20")
    for v in vals:
        if v>=0.5:
            out.append(f"   cold val {v:.4f}")
open("/tmp/fs_stats2.txt","w").write("\n".join(out)+"\n")