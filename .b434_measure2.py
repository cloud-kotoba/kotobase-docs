import subprocess, time, json, math, sys

SEARCH = "https://search.kotobase.net/search?q=test"
CTRL   = "https://kotobase.net/signup"

def batch(url, n):
    rows = []
    for i in range(n):
        try:
            r = subprocess.run(["curl","-s","-o","/dev/null","-w","%{time_starttransfer} %{time_total} %{http_code}", url], capture_output=True, text=True, timeout=60)
            p = r.stdout.split()
            rows.append([float(p[0]), float(p[1]), int(p[2])])
        except Exception:
            rows.append([999.0, 999.0, 0])
        time.sleep(0.1)
    return rows

def p50(xs):
    s = sorted(xs)
    idx = math.ceil(len(s)*0.5)-1
    return s[max(0, min(len(s)-1, idx))]

def summarize(rows:
    codes = [r[2] for r in rows]
    tt = [r[0] for r in rows]
    cold = len([x for x in tt if x>=0.5])
    warm = [x for x in tt if x<0.5]
    warmp = p50(warm) if warm else 0.0
    allp = p50(tt)
    return [sum(1 for c in codes if c==200), cold, allp, warmp, max(tt)]

tot_cold = 0
tot_ctrl_cold = 0
acc = []
for rname in ["A","B","C"]:
    srow = summarize(batch(SEARCH, 20))
    crow = summarize(batch(CTRL, 20))
    tot_cold += srow[1]
    tot_ctrl_cold += crow[1]
    acc.append([rname, srow, crow])
    print(json.dumps({"run":rname, "search":srow,"ctrl":crow}, ensure_ascii=False), flush=True)

print(json.dumps({"total_cold_search":tot_cold,"total_cold_ctrl":tot_ctrl_cold,"runs":acc}, ensure_ascii=False)