import sys

def stats(path):
    codes=[];ts=[]
    for line in open(path):
        p=line.split()
        if len(p)>=2:
            codes.append(p[0]); ts.append(float(p[1]))
    n=len(ts)
    cold=[t for t in ts if t>=0.5]
    s=sorted(ts)
    def nr(q):
        if not s: return None
        k=max(1,int(n*q/100.0+0.999999))
        return s[min(k,n)-1]
    ok=sum(1 for c in codes if c=='200')
    return n,ok,len(cold),(len(cold)/n*100 if n else 0),nr(50),nr(95),s[0] if s else None,s[-1] if s else None,cold

for label in ['A','B','C']:
    p='.c152_run575_%s.ttfb'%label
    n,ok,c,cpc,p50,p95,mn,mx,cold=stats(p)
    print('run575%s: n=%d ok=%d cold=%d (%.1f%%) p50=%.4fs p95=%.4fs min=%.4fs max=%.4fs cold_list=%s'%(label,n,ok,c,cpc,p50,p95,mn,mx,[round(x,4) for x in cold]))
n,ok,c,cpc,p50,p95,mn,mx,cold=stats('.c152_run575_landing.ttfb')
print('control: n=%d ok=%d cold=%d (%.1f%%) p50=%.4fs p95=%.4fs min=%.4fs max=%.4fs cold_list=%s'%(n,ok,c,cpc,p50,p95,mn,mx,[round(x,4) for x in cold]))
tot=0;totn=0;totok=0
for label in ['A','B','C']:
    p='.c152_run575_%s.ttfb'%label
    for line in open(p):
        q=line.split()
        if len(q)>=2:
            totn+=1; totok+= (q[0]=='200')
            if float(q[1])>=0.5: tot+=1
print('TOTAL_SEARCH n=%d ok=%d cold=%d (%.1f%%)'%(totn,totok,tot,tot/totn*100 if totn else 0))
