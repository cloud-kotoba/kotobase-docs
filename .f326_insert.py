#!/usr/bin/env python3
# Append falsify run326 K-Z3 evidence to the single K-Z3 hypothesis row (line 279).
import io, sys

PATH = "query-cosientist.md"

with io.open(PATH, encoding="utf-8") as f:
    lines = f.readlines()

# locate K-Z3 hypothesis row (physical line whose prefix is "| K-Z3 | worker |")
target = None
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 | worker |"):
        target = i
        break
assert target is not None, "K-Z3 row not found"

# The row cell END: line has no trailing "|" (per memory K-Z3 evidence cell is open-ended)
INS = (
    " falsify 2026-09-07 (第151回, K-Z3 7\u6642\u53f0 n \u7a4d\u307f\u5897\u3057 run326A\u2013C, "
    "\u540c\u6e2b\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, Tokyo, "
    "07:47:2x\u201307:48:0x JST, \u5168 80/80 200, \u6b63 endpoint search.kotobase.net/search?q=test, "
    "host load1 132.62\u2013143.22 (\u6e08\u5b9a\u6642\u7b2b, \u6982\u5ea6\u884c\u72ec gate \u5916) "
    "\u306f production HTTP \u5b9f\u6e2b\u306e\u305f\u3081 gate \u5916, secret \u4e0d\u542b \u2014 curl \u306e\u307f): "
    "cold(>=0.5s) 2/0/0 per 20 = 2/60 (~3.3%) \u2014 run326A \u6563\u767a 2/20 (idx9 1.5311s / idx14 0.8244s \u5358\u767a\u6563\u767a\u914d\u7f6e, "
    "warm \u7fa4 0.04\u20130.19s \u3067 cold \u3068\u4ea4\u4e92) p50 65.8ms / run326B cold 0/20 p50 57.7ms max 217.6ms / run326C cold 0/20 p50 58.9ms max 132.8ms, "
    "control (kotobase.net/signup) cold 0/20 p50 46.3ms max 126.2ms \u5b8c\u5168\u9759\u7a4f\u3067 control \u5206\u96e2\u6210\u7acb\u3001cold \u7fa4\u306f search \u5074\u306b\u5c40\u5728\u3002"
    "run326A \u6563\u767a 2/20 \u306f B/C 0/20 + control 0/20 \u3067\u300c\u5e2f\u5185 1 \u7a93\u5373\u6d88\u5931\u300d\u6563\u767a\u5358\u767a\u578b\u7d99\u7d9a "
    "(run322-indep 2/20, run323A 1/20, run325A 1/20 \u306e\u6563\u767a\u6e1b\u5f31\u5e45\u5f53\u5185, heavy \u306f run271A 6/20 \u4ee5\u964d 51 \u30bb\u30c3\u30c8\u9023\u7d9a\u975e\u518d\u73fe)\u3002"
    "7\u6642\u53f0 clean separable \u901a\u7b97 (rank143) = run321 (3/60) + run322-indep (2/60) + run323 (1/60) + run325 (1/60) + \u2464\u5f53 tick run326 (2/60) = 9/300 (~3.0%) \u4f4e\u4f4d\u5e2f\u5019\u88dc\u3067"
    "\u6df1\u591c\u5e2f\u4f4e\u4f4d\u5e2f\u6b8b\u754c (~1.7\u20132.0%) \u3068\u540c\u6c34\u6e96\u3001\u6df1\u591c\u5e2f traffic \u6700\u4f4e\u5e2f\u3067\u306e\u6563\u767a\u518d\u51fa\u73fe\u306f K-Z3 traffic \u4f9d\u5b58\u8aac\u3078\u306e\u53cd\u8a3c\u6750\u6599\u3092\u7d9a\u884c "
    "(\u6df1\u591c\u5e2f ~26\u201331% \u5e73\u5766\u30d1\u30bf\u30fc\u30f3\u3068\u6574\u5408\u65b9\u5411, \u5e2f\u6c34\u6e96\u78ba\u5b9a\u306f\u8ffd\u52a0 clean-tick n \u8981)\u3002status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002"
)

lines[target] = lines[target].rstrip("\n") + INS + "\n"

with io.open(PATH, "w", encoding="utf-8") as f:
    f.writelines(lines)

print("appended to line", target + 1)