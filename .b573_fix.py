import glob

for p in sorted(glob.glob(".b573_*.ttfb")):
    with open(p, encoding="utf-8") as f:
        raw = f.read()
    # repair: lines that are bare numbers are the %{time_starttransfer} half
    # of a pair whose code half landed on the previous line (curl -w newline
    # emission race seen when two curl invocations overlap output).
    toks = []
    for line in raw.split("\n"):
        line = line.strip()
        if not line:
            continue
        toks.append(line)
    pairs = []
    i = 0
    while i < len(toks):
        cur = toks[i]
        if cur.startswith("2") or cur.startswith("3") or cur.startswith("4") or cur.startswith("5"):
            code = cur
            # next bare number is the ttfb
            if i + 1 < len(toks):
                ttfb = toks[i + 1]
                i += 2
            else:
                ttfb = "0"
                i += 1
        else:
            # bare ttfb without code (shouldn't happen at start)
            code = "000"
            ttfb = cur
            i += 1
        pairs.append((code, ttfb))
    with open(p, "w", encoding="utf-8") as f:
        for code, ttfb in pairs:
            f.write("%s %s\n" % (code, ttfb))
    print(p, "pairs=", len(pairs))
