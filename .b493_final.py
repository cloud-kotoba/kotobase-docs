B="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b493"
def nearest_rank(sorted_vals, q):
    i=max(0, min(len(sorted_vals)-1, round(q*(len(sorted_vals)-1))))
    return sorted_vals[i]
outlines=[]
for lid in ["A","B","C","landing"]:
    vals=[float(x) for x in open(f"{B}_{lid}.ttfb") if x.strip()!=b""]
    vals=[float(x) for x in open(f"{B}_{lid}.ttfb")] if False else vals
    s=sorted(vals)
    p50=nearest_rank(s,0.5); p95=nearest_rank(s,0.95)
    cold=[v for v in vals if v>=0.5]
    outlines.append(f"{lid}: n={len(vals)} p50={p50:.4f} p95={p95:.4f} max={s[-1]:.4f} cold={len(cold)}/20")
    for v in vals:
        if v>=0.5:
            outlines.append(f"  cold {v:.4f}")
res="\n".join(outlines)+"\n"
with open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b493_final.txt","w") as fh:
    fh.write(res)
print(res)