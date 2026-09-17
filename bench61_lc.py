import math
p = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/bench61_run175_out.txt"
lc = []
for line in open(p):
    parts = line.split()
    if len(parts) >= 4 and parts[0] == "LC":
        lc.append((float(parts[2]), int(parts[3])))
times = sorted(t for t, c in lc)
print("LC n=%d all200=%s cold=%d p50=%.3f max=%.3f" % (len(lc), all(c == 200 for t, c in lc), sum(1 for t, c in lc if t >= 0.5), times[math.ceil(0.5 * len(times)) - 1], max(t for t, c in lc)))
