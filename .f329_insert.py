#!/usr/bin/env python3
"""falsify 153: append run330-indep evidence to K-Z3 L279 END + insert iter-log at top."""
import sys

path = "query-cosientist.md"
with open(path, encoding="utf-8") as f:
    lines = f.readlines()

# --- 1) K-Z3 row: line index 278 (1-based 279) append at END ---
ev = (
    " falsify 2026-09-07 (\u7b2c153\u56de, K-Z3 8\u6642\u53f0(9/7) independent n-add run330A\u2013C"
    " \u2014 \u540c\u6642\u8a08\u6e2c\u306e bench \u7b2c139\u56de (08:16, 0/60) \u304c run329 \u3092\u5148\u884c\u4f7f\u7528\u306e\u305f\u3081"
    " run330 \u306b\u8aad\u66ff (\u72ec\u7acb 2 \u56de\u76ee, run216/run256/run322-indep \u524d\u4f8b),"
    " \u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, Tokyo, 08:19:20\u2013 08:19:5x JST,"
    " \u5168 80/80 200, \u6b63 endpoint search.kotobase.net/search?q=test, host load1 88-102 (gate 7.5 \u5927\u5e45\u8d85\u904e)"
    " \u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916, secret \u4e0d\u542b \u2014 curl \u306e\u307f):"
    " cold(>=0.5s) 0/0/0 per 20 = 0/60 \u5b8c\u5168\u9759\u7a4f \u2014 run330A 0/20 p50 181.4ms max 236.0ms /"
    " run330B 0/20 p50 166.7ms max 263.8ms / run330C 0/20 p50 99.3ms max 277.6ms,"
    " control (kotobase.net/signup) cold 0/20 p50 109.0ms max 234.5ms \u5b8c\u5168\u9759\u7a4f\u3067 control \u5206\u96e2\u6210\u7acb"
    " (search/control \u3068\u3082 0 cold). run330 \u5168 0/60 \u5b8c\u5168\u9759\u7a4f\u306f bench \u7b2c139\u56de run329 (0/60, 08:16)"
    " \u3068\u540c 8\u6642\u53f0\u30a6\u30a3\u30f3\u30c9\u3067\u72ec\u7acb\u7d2f\u8a08 2 \u30bb\u30c3\u30c8\u9023\u7d9a\u306e\u518d\u9759\u7a4f\u3067\u3001"
    " falsify152-run328 (1/60) \u5358\u767a\u76f4\u5f8c\u306e\u518d\u9759\u7a4f\u300c\u5e2f\u5185 1 \u7a93\u5373\u6d88\u5931\u300d\u5206\u6563\u5358\u767a\u578b\u3092\u7d99\u7d9a\u652f\u6301,"
    " heavy run271A 6/20 \u578b\u306f run271A \u4ee5\u964d 55 \u30bb\u30c3\u30c8\u9023\u7d9a\u975e\u518d\u73fe."
    " 8\u6642\u53f0 (9/7) clean separable \u901a\u7b97 = falsify152-run328 (1/60) + bench139-run329 (0/60) + \u672c tick run330 (0/60)"
    " = 1/180 (~0.56%) \u306e 3 \u30bb\u30c3\u30c8\u4f4e\u4f4d\u5e2f\u5019\u88dc \u2014 host load \u9ad8\u9a30 (88-102) \u3067 p50 \u4e0a\u632f\u308c (99-181ms) borderline note"
    " \u3060\u304c\u5168 max 278ms \u672a\u6e80\u3067 cold \u95d8\u5024 0.5s \u672a\u9054, 0/60 \u5224\u5b9a\u306f\u78ba\u5b9a\u7684."
    " status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)."
)
# append to end of K-Z3 line (index 278)
lines[278] = lines[278].rstrip("\n") + ev + "\n"
print("K-Z3 line 279 appended, new len", len(lines[278]))
# verify run330 appears once
cnt = lines[278].count("run330A\u2013C")
print("run330A-C occurrences in L279:", cnt)

# --- 2) insert iter-log entry (newest-first) after '## Iteration log' header ---
log_ln = None
for i, x in enumerate(lines):
    if x.startswith("## Iteration log"):
        log_ln = i
        break
assert log_ln is not None, "iter log header not found"
ilog_entry = (
    "- 2026-09-07: **falsify \u7b2c153\u56de**\u300208:19 JST tick\u3002HEAD 4e24a24 = bench \u7b2c139\u56de (08:16, 8\u6642\u53f0 run329 0/60)"
    " = remote net-kotobase/main \u4e00\u81f4 (fetch + rev-parse \u6bd4\u8f03, \u508d\u96e2 0; worktree detached HEAD \u306e\u305f\u3081 git pull --ff-only \u4e0d\u53ef,"
    " fetch \u7cfb\u3067\u53d6\u308a\u8fbc\u307f)\u3002live smoke 200 (/, /signup; pre-run \u8a08\u6e2c)\u3002host load1 121.35 (08:15 uptime) \u2192 88-102 (08:19 \u6e2c\u5b9a\u6642, gate 7.5 \u5927\u5e45\u8d85\u904e)"
    " \u306e\u305f\u3081 local \u6e2c\u5b9a\u306f\u62d2\u5426\u3057 production HTTP \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af (gate \u5916)\u3002"
    "\u203b\u4e88\u5b9a\u30e2\u30cb\u30bf NEXT\u300cK-Z3 \u6df1\u591c\u5e2f 23\u6642\u53f0 n \u7a4d\u307f\u5897\u3057\u7d99\u7d9a\u300d\u306f stale (rank \u7b2c90\u56de\u5e2f artifact)"
    " \u2014 true progressive NEXT \u306f rank \u7b2c144\u56de bump \u6e08\u307f\u300cK-Z3 current-band(8hr) n-add run329\u300d\u304c\u6b63\u300d\u3068\u3057\u305f\u304c,"
    " \u540c tick \u306b bench \u7b2c139\u56de\u304c run329 (08:16, 0/60) \u3092\u5148\u884c commit \u3057\u305f\u305f\u3081"
    " \u672c tick \u306e\u5b9f\u6e2c (08:19, K-Z3 8\u6642\u53f0 n \u7a4d\u307f\u5897\u3057\u3068\u3057\u3066 run330 \u306b\u8aad\u66ff \u2014 run216/run256/run322-indep \u524d\u4f8b\u3067\u72ec\u7acb 2 \u8a08\u6e2c\u8a18\u9332)\u3002"
    " K-Z3 8\u6642\u53f0 run330A\u2013C \u3092\u672c tick \u5b9f\u6e2c (same \u6e2c\u5b9a\u6cd5 n=20\u00d73 + landing control, \u5225\u63a5\u7d9a curl, cold>=0.5s, nearest-rank p50, 08:19:20 JST, \u5168 80/80 200):"
    " A cold 0/20 p50 181.4ms / B cold 0/20 p50 166.7ms / C cold 0/20 p50 99.3ms / control (kotobase.net/signup) 0/20 p50 109.0ms max 234.5ms \u5b8c\u5168\u9759\u7a4f\u3067 control \u5206\u96e2\u6210\u7acb\u3001"
    " cold \u7fa4 search \u5074\u306b\u5c40\u5728 \u2014 search cold 0/60 \u5b8c\u5168\u9759\u7a4f\u3001bench-run329 (08:16, 0/60) \u3068\u540c 8\u6642\u53f0\u30a6\u30a3\u30f3\u30c9\u72ec\u7acb\u7d2f\u8a08 2 \u30bb\u30c3\u30c8\u9023\u7d9a\u518d\u9759\u7a4f\u3001"
    " \u5206\u6563\u5358\u767a\u578b\u300c\u5e2f\u5185 1 \u7a93\u5373\u6d88\u5931\u300d\u7d99\u7d9a (heavy run271A 6/20 \u578b\u306f run271A \u4ee5\u964d 55 \u30bb\u30c3\u30c8\u9023\u7d9a\u975e\u518d\u73fe)\u3002"
    " 8\u6642\u53f0 (9/7) clean separable \u901a\u7b97 = falsify152-run328 (1/60) + bench139-run329 (0/60) + \u672c tick run330 (0/60) = 1/180 (~0.56%) \u306e 3 \u30bb\u30c3\u30c8\u4f4e\u4f4d\u5e2f\u5019\u88dc\u3002"
    " \u8a73\u7d30\u306f K-Z3 evidence \u6b04 (L279 \u672b\u5c3e\u8ffd\u8a18)\u3002status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002secret \u306f\u4e00\u5207\u8a18\u9332\u305b\u305a\u3002"
)
lines.insert(log_ln + 1, ilog_entry + "\n")
print("iter-log inserted at line", log_ln + 2)

with open(path, "w", encoding="utf-8") as f:
    f.writelines(lines)
print("written OK")