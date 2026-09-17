import subprocess, json, time, statistics

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

def summary(name, codes, ttfbs):
    colds = [t for t in ttfbs if t >= COLD]
    warms = sorted(t for t in ttfbs if t < COLD)
    # nearest-rank p50 over all 20
    s = sorted(ttfbs)
    p50 = s[int(0.50 * len(s) + 0.999) - 1]
    line = ("%s all=%d ok=%d cold(>=%.1fs)=%d p50=%.3fs" %
            (name, len(ttfbs), sum(1 for c in codes if c == 200), len(colds), COLD, p50))
    if colds:
        line += " colds=%s" % (" ".join("%.3fs(#%d)" % (t, ttfbs.index(t) + 1) for t in colds))
    if warms:
        line += " warm range=%.3f-%.3f" % (warms[0], warms[-1])
    return line

out = []
out.append("time: %s" % time.strftime("%Y-%m-%d %H:%M:%S JST"))
for tag, url in (("run117A", SEARCH), ("run117B", SEARCH), ("run117C", SEARCH),
                 ("landing-control", LANDING)):
    codes, ttfbs = run_seq(url)
    out.append(summary(tag, codes, ttfbs))
open("/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench41_out.txt", "w").write("\n".join(out) + "\n")
