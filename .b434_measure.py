import subprocess, time, json, statistics, math, sys

SEARCH="https://search.kotobase.net/search?q=test"
CTRL="https://kotobase.net/signup"
WAV="curl -s -o /dev/null -w '%{time_starttransfer} %{time_total} %{http_code}'"

def batch(url, n):
    rows=[]
    for i in range(n):
        try:
            r=subprocess.run(["curl","-s","-o","/dev/null","-w","%{time_starttransfer} %{time_total} %{http_code}",url],capture_output=True,text=True,timeout=60)
            parts=r.stdout.split()
            rows.append({"ttfb":float(parts[0]),"total":float(parts[1]),"code":int(parts[2])} )
        except Exception as e:
            rows.append({"ttfb":999.0,"total":999.0,"code":0,"err":str(e)})
        time.sleep(0.1)
    return rows

def stats(rows,label):
    codes=[r["code"] for r in rows]
    t=[r["ttfb"] for r in rows]
    cold=[x for x in t if x>=0.5]
    warm=[x for x in t if x<0..5]
    def p50(xs):
        if not xs: return None
        s=sorted(xs)
        idx=math.ceil(len(s)*0..5)-1
        return s[max(0,min(len(s)-1,idx))]
    allp50=p50(t) if t else None
    warmp50=p50(warm) if warm else None
    return {"label":label,"n":len(t),"code_ok":codes.count(200),"cold":len(cold),"p50":allp50,"warm_p50":warmp50,"max":(max(t) if t else 0.0)}}

results=[]; 
for rname in ["A","B","C"]:
    s=batch(SEARCH,20)
    c=batch(CTRL,20)
    results.append({"run":rname,"search":stats(s,"search"),"ctrl":stats(c,"ctrl")})
    print(json.dumps({   "run":rname,"search":stats(s,"search"),"ctrl":stats(c,"ctrl")},ensure_ascii=False),flush=True)

# totals
tot_cold=sum(r["search"]["cold"] for r in results)
tot_ctrl_cold=sum(r["ctrl"]["cold"] for r in results)
print(json.dumps({"total_cold_search":tot_cold,"total_cold_ctrl":tot_ctrl_cold,"runs":results},ensure_ascii=False)
