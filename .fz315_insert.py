#!/usr/bin/env python3
import io

PATH = "query-cosientist.md"
ADDS = " falsify 2026-09-07 (\u7b2c145\u56de, K-Z3 6\u6642\u53f0(\u6df1\u591c\u5e2f\u304b\u3089\u671d\u306e\u5e2f\u7956) n \u7a4d\u307f\u5897\u3057 run315A\u2013C \u2014 rank \u7b2c138\u56de NEXT\u300ccurrent-band n-add, \u6642\u9593\u5e2f\u79fb\u884c\u5f8c\u306f\u6b21\u306e\u5e2f\u521d\u3078\u300d\u306e\u7d99\u7d9a\u67a0 (\u73fe\u6642\u523b 05:58\u201306:01 JST \u3067 6\u6642\u53f0\u5e2f\u521d), \u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, Tokyo, 06:00\u201306:01 JST, \u5168 80/80 200, \u6b63 endpoint search.kotobase.net/search?q=test, host load1 18.47 (06:01 uptime \u5b9f\u6e2c, gate 7.5 \u5927\u5e45\u8d85\u904e) \u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916, secret \u4e0d\u542b \u2014 curl \u306e\u307f): cold(>=0.5s) 2/0/0 per 20 = 2/60 \u2014 run315A cold 2/20 (1.536s 5\u756a\u76ee + 0.851s 6\u756a\u76ee \u306e\u9023\u7d9a\u30da\u30a2, \u5e2f\u521d\u306e\u6563\u767a\u5bfe\u5024) p50 41.1ms / run315B cold 0/20 p50 40.1ms max 53.7ms / run315C cold 0/20 p50 39.4ms max 57.0ms, control (kotobase.net/signup) cold 0/20 p50 50.6ms max 310.6ms \u3067 control \u5206\u96e2\u6210\u7acb (cold \u7fa4\u306f search A \u306e 5-6\u756a\u76ee\u306e\u307f\u306b\u5c40\u5728, control \u306f 0 cold \u3060\u304c max 310.6ms \u306e\u5358\u767a\u7d0d\u3070\u3064\u304d\u3042\u308a). run315 \u306f run312-313-314 \u5b8c\u5168\u9759\u5f13 3 \u9023\u7d9a\u3092\u5272\u308a\u3001\u5e2f\u521d (6\u6642\u53f0) \u3067\u6563\u767a\u30da\u30a2 2/60 \u3092\u518d\u73fe (run310 2/60 / run311 1/60 \u578b\u306e\u6563\u767a\u5358\u767a/\u30da\u30a2 = \u5373\u6d88\u5931\u306e\u6027\u8cea\u3068\u6574\u5408, heavy \u30af\u30e9\u30b9\u30bf run271A 6/20 \u578b\u306f run271A \u4ee5\u964d 40 \u30bb\u30c3\u30c8\u9023\u7d9a\u975e\u518d\u73fe)\u3002deep-night \u7d2f\u8a08 run275..314 = 40/2400 (~1.67%) 40\u30bb\u30c3\u30c8\u306f\u5909\u308f\u3089\u305a\u4f4e\u4f4d\u5e2f\u6c34\u6e96\u30016\u6642\u53f0\u5e2f\u521d\u306e 2/60 \u306f\u663c\u65e5\u5e2f\u3078\u306e\u79fb\u884c\u5e2f\u3067\u6563\u767a\u518d\u73fe\u306e\u5206\u6790\u6750\u81a8\u3002status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002"

lines = io.open(PATH, encoding="utf-8").read().split("\n")
# K-Z3 row is line index 278 (0-based) = line 279 (1-based)
idx = 278
assert lines[idx].lstrip().startswith("| K-Z3 |"), (idx, lines[idx][:80])
old_len = len(lines[idx])
lines[idx] = lines[idx] + ADDS
new_len = len(lines[idx])
open(PATH, "w", encoding="utf-8").write("\n".join(lines))
print(f"OK line279 len {old_len}->{new_len}")
big = open(PATH, encoding="utf-8").read()
print("occur run315A:", big.count("run315A"))
print("occur 5-6\u756a\u76ee:", big.count("5-6\u756a\u76ee"))