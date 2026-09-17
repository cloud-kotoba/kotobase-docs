#!/usr/bin/env python3
# falsify run295 evidence insert: append new evidence row after latest commit row
# (anchor = bench 2026-09-07 第121回 row, line-start ASCII-prefix match, no en-dash)
ANCHOR = "bench 2026-09-07 (第121回"
NEW = (
"falsify 2026-09-07 (第135回, K-Z3 3時台(深夜帯) n 積み増し run295A\u2013C \u2014 "
"bench 第121回 run294 (03:23) に続く 3時台 n 積み増し (次 run ID run295), "
"同測定法 n=20 \u00d7 3 + landing control, 別接続 curl, Tokyo, 03:31:17\u201303:31:24 JST, "
"全 80/80 200, 正 endpoint search.kotobase.net/search?q=test, host load1 38.95 (03:31 uptime "
"\u5b9f\u6e2c, gate 7.5 \u5927\u5e45\u8d85\u904e) \u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916, "
"secret \u4e0d\u542b \u2014 curl \u306e\u307f): "
"cold(>=0.5s) 1/1/0 per 20 = 2/60 (~3.3%) \u2014 "
"run295A \u5358\u767a\u6563\u767a 1.3076s p50 44.2ms / run295B \u5358\u767a\u6563\u767a 0.9367s p50 41.9ms / run295C cold 0/20 p50 40.5ms max 61.8ms, "
"control (kotobase.net/signup) cold 0/20 p50 41.9ms max 112.8ms \u5b8c\u5168\u9759\u7a4f\u3067 control \u5206\u96e2\u6210\u7acb\u3001cold \u7fa4\u306f search \u5074\u306b\u5c40\u5728\u3002"
"run295A/B \u5404\u5358\u767a\u306f C 0/20 + control 0/20 \u3067\u5373\u6d88\u5931\u3057\u300c\u5e2f\u5185 1 \u7a93\u5373\u6d88\u5931\u300d"
"\u6563\u767a\u5358\u767a\u578b\u7d99\u7d9a (heavy \u30af\u30e9\u30b9\u30bf\u306f run271A \u4ee5\u964d 22 \u30bb\u30c3\u30c8\u975e\u518d\u73fe)\u3002"
"3\u6642\u53f0\u901a\u7b97 (falsify run291 2/60 + bench run292 1/60 + falsify run293 0/60 + bench run294 2/60 + \u672c tick 2/60) "
"= 7/300 (~2.3%) \u306e 5 \u30bb\u30c3\u30c8\u3001deep-night \u7d2f\u8a08 run275..295 = 29/1320 (~2.2%) \u306e 22 \u30bb\u30c3\u30c8\u3067\u4f4e\u4f4d\u5e2f\u6c34\u6e96\u7d9a\u4f4d \u2014 "
"\u6df1\u591c\u6700\u4f4e\u5e2f (traffic \u6700\u4f4e) \u3067\u306e cold \u6563\u767a\u518d\u51fa\u73fe (run293 \u5b8c\u5168\u9759\u7a4f 0/60 \u2192 run294 2/60 \u2192 \u672c tick 2/60) \u306f "
"K-Z3 traffic \u4f9d\u5b58\u8aac\u3078\u306e\u53cd\u8a3c\u6750\u6599\u3092\u7d9a\u884c (\u6df1\u591c\u5e2f ~26-31% \u5e73\u5766\u30d1\u30bf\u30fc\u30f3\u3068\u6574\u5408\u65b9\u5411)\u3002status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002"
)

path = "query-cosientist.md"
lines = open(path, encoding="utf-8").read().split("\n")
# find anchor line (the bench 121 evidence row, starts with ANCHOR)
idx = None
for i, ln in enumerate(lines):
    if ln.startswith(ANCHOR):
        idx = i
        break
if idx is None:
    raise SystemExit("ANCHOR_NOT_FOUND")
# verify uniqueness
cnt = sum(1 for ln in lines if ln.startswith(ANCHOR))
if cnt != 1:
    raise SystemExit(f"ANCHOR_COUNT={cnt} EXPECTED 1")
full = "\n".join(lines)
# build new file with NEW inserted right after anchor line
newlines = lines[:idx+1] + [NEW] + lines[idx+1:]
open(path, "w", encoding="utf-8").write("\n".join(newlines))
print("INSERTED after line", idx+1)