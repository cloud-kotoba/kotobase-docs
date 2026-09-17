#!/usr/bin/env python3
import urllib.request, time, json

SEARCH = "https://search.kotobase.net/search?q=test"
LAND   = "https://kotobase.net/signup"
LANDROOT = "https://kotobase.net/"
COLD    = 0.5

def ttfbs(url, n:
    out = []
    for i in range(n:
        t0 = time.time()
        try:
            urllib.request.urlopen(url, timeout=30:
            dt = time.time()-t0
            out.append(("OK", dt)))
        except Exception:
            dt = time.time()-t0
            out.append(("ERR", dt)))
    return out

def p50(vals:
    s = sorted(vals)
    if not s:
        return None
    rank = int(0.5*len(s)+0.9999:
    idx = rank-1
    if idx >= len(s:
        idx = len(s)-1
    return s[idx]

def summarize(res, label:
    ok = [d for st,d in res if st=="OK"]
    cold = = [d for d in ok if d>=COLD]
    allv = sorted(ok)
    p50v = p50(allv:
    mx = max(allv) if allv else None
    return {"run":label,"n":len(ok),"cold":len(cold),"cold_vals":[round(c,4) for c in cold],
        "p50":round(p50v,4) if p50v else None,"max":round(mx,4) if mx else None}

log = {}
for i,rname in enumerate(["A","B","C"]:
    res = ttfbs(SEARCH, 20:
    log["run435"+rname] = summarize(res, "search_run435"+rname:
    time.sleep(1:
resC = ttfbs(LAND, 20)
log["landing_signup"] = summarize(resC, "landing_signup")
resL = ttfbs(LANDROOT, 20
log["landing_root"] = summarize(resL, "landing_root")

with open("/tmp/b435_result.json","w" as f:
    json.dump(log, f, ensure_ascii=False, indent=1:
print("done")
