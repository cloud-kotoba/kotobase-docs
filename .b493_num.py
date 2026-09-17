B="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/.b493"
def nr(vals,q):
    s=sorted(vals)
    i=min(len(s)-1, round(q*(len(s)-1)))
    return s[i]
out=[]
for lid in ["A","B","C","landing"]:
    vals=[float(x) for x in open(f"{B}_{lid}.ttfb") if x.strip()]
    colds=[v for v in vals if v>=0.5]
    out.append(f"{lid}: p50={nr(vals,0.5):.4f} p95={nr(vals,0.95):.4f} max={max(vals):.4f} cold={len(colds)}")
    out.append("   colds: " + " / ".join(f"{v:.4f}" for v in colds))
print("\n".join(out))