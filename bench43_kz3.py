import subprocess, time

N = 20
COLD = 0.5
SEARCH = "https://search.kotobase.net/search?q=test"
LANDING = "https://kotobase.net/"

def run_seq(url, n=N):
    ttfbs = []
    codes = []
    for _ in range(n):
        r = subprocess.run(
            ["curl", "-o", "/dev/null", "-s", "-w", "%{http_code} %{time_starttransfer}", url],
            capture_output=True, text=True, timeout=30)
        parts = r.stdout.split()
        codes.append(int(parts[0]))
        ttfbs.append(float(parts[1]))
    return codes, ttfbs

def summary(name, codes, ttfbs, cold_th=COLD):
    colds = [t for t in ttfbs if t >= cold_th]
    warms = sorted(t for t in ttfbs if t < cold_th)
    s = sorted(ttfbs)
    p50 = s[int(0.50 * len(s) + 0.999) - 1]
    line = ("%s all=%d ok=%d cold(>=%.1fs)=%d p50=%.3fs" %
            (name, len(ttfbs), sum(1 for c in codes if c == 200), cold_th, len(colds), p50))
    if colds:
        line += " colds=%s" % (" ".join("%.3fs(#%d)" % (t, ttfbs.index(t) + 1) for t in colds))
    if warms:
        line += " warm range=%.3f-%.3f" % (warms[0], warms[-1])
    return line

out = []
out.append("time: %s" % time.strftime("%Y-%m-%d %H:%M:%S JST"))
for tag, url in (("run122A", SEARCH), ("run122B", SEARCH), ("run122C", SEARCH),
                 ("landing-control", LANDING)):
    codes, ttfbs = run_seq(url)
    out.append(summary(tag, codes, ttfbs))
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench43_out.txt", "w").write("\n".join(out) + "\n")
print("\n".join(out))
