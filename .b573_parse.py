import re

# Recover (code, ttfb) pairs from .b573_A.ttfb.bak raw capture.
# Format anomalies observed:
#  - lines '000 <ttfb>': code fragment lost (two curls raced on one line),
#    the number present IS a valid ttfb sample.
#  - lines '2.015615 0.051945' / '2.067020 1.930322' / '2.384378 1.201077':
#    a ttfb sample (2.015615 etc.) merged with a following 'code ttfb' pair.
#  - lines '<code> <ttfb> <code> <ttfb>': two pairs on one line.
# Strategy: token-stream scan; a token is either a 3-digit code (200/000/3xx..)
# or a float. Consume greedily: code followed by ttfb = one sample; a bare
# float with lost code counts as a sample with unknown code (timing valid).

CODE_RE = re.compile(r"^\d{3}$")
FLOAT_RE = re.compile(r"^\d+\.\d+$")

def parse(path):
    toks = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split()
            # unmerge glued '<float><code> <ttfb>' like '2.015615 0.051945'
            # where first token is float>999 style e.g. '2.015615' -> that's a
            # ttfb, not a code. codes are exactly 3 digits.
            toks.extend(parts)
    samples = []
    i = 0
    while i < len(toks):
        t = toks[i]
        if CODE_RE.match(t):
            code = t
            if i + 1 < len(toks) and FLOAT_RE.match(toks[i + 1]):
                # if next-next token exists and is also float and this float
                # has 7 sig decimals like ttfb, fine - it is the ttfb of this code
                samples.append((code, float(toks[i + 1])))
                i += 2
            else:
                # code without ttfb -> skip
                i += 1
        elif FLOAT_RE.match(t):
            # bare ttfb, code lost
            samples.append(("???", float(t)))
            i += 1
        else:
            i += 1
    return samples

for p in [".b573_A.ttfb", ".b573_B.ttfb", ".b573_C.ttfb", ".b573_ctl.ttfb"]:
    s = parse(p)
    codes = [c for c, t in s]
    n200 = codes.count("200")
    unknown = codes.count("???")
    other = len(s) - n200 - unknown
    ts = sorted(t for c, t in s)
    print(p, "samples=", len(s), "200=", n200, "unknown_code=", unknown, "other=", other)
    cold = [t for c, t in s if t >= 0.5]
    print("   cold>=0.5s:", len(cold), [round(x, 4) for x in cold])
    if ts:
        print("   p50=", round(ts[len(ts)//2]*1000, 1), "ms  max=", round(ts[-1], 4), "s")
