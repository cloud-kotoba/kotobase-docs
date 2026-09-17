#!/usr/bin/env python3
# Append run405 evidence to K-Z3 row (END of the K-Z3 single-line cell) and insert iter-log entry (newest-first).
# Locates rows by content match (not hardcoded indices) since concurrent rank commits shift lines.
import sys

PATH = "/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"

with open(PATH, encoding="utf-8") as f:
    txt = f.read()

# scrub zero-width chars / problematic tokens per memory
for c in ["\u200b", "\u200c", "\u200d", "\ufeff"]:
    txt = txt.replace(c, "")

lines = txt.split("\n")

# locate K-Z3 row: line starts with "| K-Z3 | worker |"
kz3_idx = None
for i, ln in enumerate(lines):
    if ln.startswith("| K-Z3 | worker |"):
        kz3_idx = i
        break
assert kz3_idx is not None, "K-Z3 row not found"

# locate iter-log header
ilog_idx = None
for i, ln in enumerate(lines):
    if ln.strip() == "## Iteration log":
        ilog_idx = i
        break
assert ilog_idx is not None, "Iteration log header not found"

print("K-Z3 row at line", kz3_idx + 1)
print("Iteration log at line", ilog_idx + 1)

ev = (" falsify 2026-09-07 (\u7b2c177\u56de, K-Z3 23\u6642\u53f0 n \u7a4d\u307f\u5897\u3057 run405A\u2013C \u2014 iter-log HEAD (rank \u7b2c172\u56de) \u300cNEXT: K-Z3 22/23\u6642\u53f0 n \u7a4d\u307f\u5897\u3057\u7d9a\u884c \u2026 \u6b21 run ID \u306f run404 \u4f7f\u7528\u300d\u306e\u7d9a\u884c\u67a0\uff08run404 \u306f bench \u7b2c183\u56de (23:04) \u304c\u5148\u884c\u4f7f\u7528\u6e08\u307f\u306e\u305f\u3081 run405 \u306b\u8aad\u66ff \u3001run216/run256/run263/run403 \u524d\u4f8b\u306e same-band independent \u8a08\u6e2c\uff09, "
 "same \u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, cold>=0.5s, nearest-rank p50, \u6b63 endpoint search.kotobase.net/search?q=test, 23:32:46\u201323:33:14 JST, "
 "\u5168 80/80 200, host load1 17.03\u219218.08 (23:32/23:33 uptime \u5b9f\u6e2c, gate 7.5 \u8d85\u904e) \u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916, secret \u4e0d\u542b \u2014 curl + python stats \u306e\u307f): "
 "cold(>=0.5s) 7/1/3 per 20 = 11/60 (~18.3%) \u2014 run405A cold 7/20 \u6df1\u3044\u6563\u767a/heavy \u30af\u30e9\u30b9\u30bf (0.9276s/2.4846s/1.5645s/1.9714s/1.8939s/1.3711s/2.4782s \u6563\u767a\u914d\u7f6e, deep 2.48s \u542b\u3080) p50 100.4ms max 2484.6ms "
 "/ run405B cold \u5358\u767a 1/20 (1.235s) p50 53.3ms / run405C cold 3/20 (0.695s/1.2479s/0.6803s \u6563\u767a) p50 66.9ms, control (kotobase.net/signup) cold 3/20 (0.5062s/0.6473s/0.5628s \u5883\u754c\u5024 \u9003\u3001\u3059\u3079\u3066 0.5\u20130.65s \u5883\u754c\u30d0\u30f3\u30c9) "
 "p50 53.2ms max 647.3ms \u2014 control \u51b7\u51cd 3/20 \u3067\u5b8c\u5168\u9759\u7a4f\u4e0d\u6210\u7acb not-separated-leaning \u6ce8\u8a18 (search cold 11 \u4ef6\u306e\u3046\u3061 405A \u306e 7 \u4ef6\u306f 0.93\u20132.48s deep \u3067 control \u5883\u754c 0.5\u20130.65s \u3068\u9006\u65b9\u5411\u306e magnitude \u5206\u96e2\u5f31\u6210\u7acb, cold \u6fc3\u5ea6\u306f search 11/60 \u5bfe control 3/20 \u3067 search \u5074\u306b\u6fc3\u3044\u304c control \u5883\u754c 3 \u4ef6\u3067\u5b8c\u5168\u9759\u7a4f\u3067\u306f\u306a\u3044 \u2014 version \u30cd\u30c3\u30c8\u30ef\u30fc\u30af/host load \u6df7\u5165\u53ef\u80fd)\u3002"
 "run405A cold 7/20 heavy \u30af\u30e9\u30b9\u30bf (\u3053\u306e 23\u6642\u53f0 9/7 \u3067\u306f run403A \u7d9a\u304d 2 \u3064\u76ee) \u306f B/C 0/40 \u5373\u6d88\u5931\u3067\u3042\u308b\u304c run405C \u3082 3/20 \u3067\u300c\u5e2f\u5185 1 \u7a93\u5373\u6d88\u5931\u300d\u578b\u7d99\u7d9a (heavy>=6/20 \u306f run403A \u3068\u540c\u6c34\u6e96\u3067\u5378\u304f\u306a\u3044)\u3002"
 "23\u6642\u53f0 (9/7) \u901a\u7b97 = falsify run403 (7/60) + bench run404 (3/60) + \u672c run405 (11/60) = 21/180 (~11.7%) \u2014 22\u6642\u53f0 (17/120 ~14.2%) \u3068\u540c\u6c34\u6e96\u306e\u9ad8\u4f4d\u5e2f\u7d99\u7d9a, \u4f46\u3057\u672c tick \u306f control \u51b7\u51cd 3/20 \u3067 not-separated-leaning (control \u5be1\u9759\u3067\u306a\u304f\u3001search cold \u304c\u30cd\u30c3\u30c8\u30ef\u30fc\u30af/host-load \u6df7\u5165\u306e\u53ef\u80fd\u6027\u3042\u308a\u300ccold \u7fa4\u306f search \u5074\u306b\u5c40\u5728\u3057\u30c8\u30e9\u30d5\u30a3\u30c3\u30af\u4f9d\u5b58\u300d\u306e K-Z3 \u4e3b\u5f35\u3068\u306f control \u5206\u96e2\u304c\u4e0d\u6210\u7acb\u306e\u53cd\u8a3c\u8cc7\u6599\u3002\u5e2f\u6c34\u6e96\u786e\u5b9a\u30fb\u6a5f\u69cb\u5224\u65ad\u306b\u306f rank \u8ffd\u52a0 n \u3092\u8981\u3059\u308b\u3002status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002NEXT: \u59d4\u306d\u308b (rank \u6307\u5b9a\u512a\u5148; \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af\u306f K-Z3 \u73fe\u5728\u6642\u523b\u5e2f 23\u6642\u53f0 n \u7a4d\u307f\u5897\u3057\u7d9a\u884c, \u6b21 run ID \u306f run406 \u4f7f\u7528)\"")

iter_entry = ("- 2026-09-07: **falsify \u7b2c177\u56de**\u300223:32 JST tick\u3002HEAD 11f80c8 = rank \u7b2c172\u56de (23:04, fold falsify175-run401+bench182-run402 -> 22hr 17/120 ~14.2% + falsify176-run403 23hr band-first 7/60 ~11.7%) = remote net-kotobase/main \u4e00\u81f4 "
 "(git fetch + rev-parse \u6bd4\u8f03, \u8fb5\u96e2 0; worktree detached HEAD \u306e\u305f\u3081 fetch \u7cfb\u3067\u53d6\u8fbc; terminal foreground stdout \u7a7a=\u65e2\u77e5\u306e\u305f\u3081\u72b6\u614b\u78ba\u8a8d\u30fb\u8a08\u6e2c\u51fa\u529b\u306f\u30d5\u30a1\u30a4\u30eb\u66f8\u304d\u51fa\u3057\u7d4c\u7531)\u3002"
 "live smoke 200 (/, /signup; pre-run \u8a08\u6e2c + \u672c tick \u5b9f\u6e2c\u5168 80/80 200)\u3002host load1 32.44 (23:15 pre-run uptime \u5b9f\u6e2c\u219218.08 23:33, gate 7.5 \u8d85\u904e) \u306e\u305f\u3081 local \u6e2c\u5b9a\u306f\u62d2\u5426 \u2014 \u4f46\u3057 K-Z3 \u89b3\u6e2c\u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916\u3067\u5b9f\u65bd\u3002"
 "\u203bpre-run monitor NEXT\u300cK-Z3 \u6df1\u591c\u5e2f 23\u6642\u53f0 n \u7a4d\u307f\u5897\u3057\u7d9a\u884c\u300d\u306f stale (rank \u7b2c90\u56de\u5e2f artifact) \u2014 true progressive NEXT \u306f iter-log HEAD (rank \u7b2c172\u56de, 23:04) \u300cNEXT: K-Z3 22/23\u6642\u53f0 n \u7a4d\u307f\u5897\u3057\u7d9a\u884c \u2026 \u6b21 run ID \u306f run404 \u4f7f\u7528\u300d\u3067\u3042\u308a\u3001cron \u5b9f\u884c\u6642\u523b 23:32 \u304c 23\u6642\u53f0 (run403 \u6e08 7/60 + run404 \u6e08 3/60) \u4e2d\u306e n \u7a4d\u307f\u5897\u3057\u7d9a\u884c\u3002"
 "run405 \u306f run404 \u304c bench \u7b2c183\u56de\u5148\u884c\u4f7f\u7528\u6e08\u307f\u306e\u305f\u3081 read\u66ff (run403 \u5411\u3051\u306e NEXT \u60c5\u5831\u3068\u306f\u7570\u306a\u308a\u3001run405 \u306f commit \u672a\u4f7f\u7528\u30fb.b405 \u65e2\u5b58\u306a\u3057=\u885d\u7a81\u306a\u3057\u78ba\u8a8d)\u3002"
 "run405 \u5b9f\u6e2c (same \u6e2c\u5b9a\u6cd5 n=20 x 3 + landing control, \u5225\u63a5\u7d9a curl, cold>=0.5s, nearest-rank p50, \u6b63 endpoint search.kotobase.net/search?q=test, 23:32:46\u201323:33:14 JST, \u5168 80/80 200, secret \u4e0d\u542b \u2014 curl + python stats \u306e\u307f): "
 "cold(>=0.5s) 7/1/3 per 20 = 11/60 (~18.3%) \u2014 run405A cold 7/20 heavy \u6563\u767a\u30af\u30e9\u30b9\u30bf (deep 2.48s \u542b\u3080, 0.93\u20132.48s) p50 100.4ms / run405B \u5358\u767a 1/20 (1.235s) p50 53.3ms / run405C 3/20 (0.68\u20130.7s \u5883\u754c) p50 66.9ms, "
 "control (kotobase.net/signup) cold 3/20 (0.5062s/0.6473s/0.5628s \u5883\u754c\u5024) p50 53.2ms \u2014 control \u51b7\u51cd 3/20 \u3067\u5b8c\u5168\u9759\u7a4f\u4e0d\u6210\u7acb not-separated-leaning (search cold 405A \u306f deep \u3067 magnitude \u5206\u96e2\u5f31\u6210\u7acb\u3059\u308b\u304c control \u5883\u754c 3 \u4ef6\u3067\u5b8c\u5168\u9759\u7a4f\u3067\u306f\u306a\u3044\u3002network/host-load \u6df7\u5165\u53ef\u80fd \u2014 K-Z3 \u4e3b\u5f35\u3078\u306e control \u5206\u96e2\u4e0d\u6210\u7acb\u53cd\u8a3c\u8cc7\u6599)\u3002"
 "23\u6642\u53f0 (9/7) \u901a\u7b97 = run403 (7/60) + run404 (3/60) + run405 (11/60) = 21/180 (~11.7%) \u3067 22\u6642\u53f0 (17/120 ~14.2%) \u3068\u540c\u6c34\u6e96\u306e\u9ad8\u4f4d\u5e2f\u7d99\u7d9a \u2014 \u4f46\u3057 run \u7d9a\u304d control \u51b7\u51cd\u4f34\u3044\u306e not-separated \u3067\u30c8\u30e9\u30d5\u30a3\u30c3\u30af\u4f9d\u5b58\u8aac\u3078\u306e\u6c7a\u5b9a\u7684\u53cd\u8a3c/definitive \u652f\u6301\u306b\u306f\u672a\u9054 (control \u5206\u96e2\u6210\u7acb\u30bd\u30fc\u30c8\u306e\u5f97\u3089\u308c\u3066\u3044\u306a\u3044)\u3002status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002secret \u306f\u4e00\u5207\u8a18\u9332\u305b\u305a\u3002\u8a73\u7d30\u306f K-Z3 evidence \u6b04 (L279 \u672b\u5c3e) \u8ffd\u8a18\u3002NEXT: \u59d4\u306d\u308b (rank \u6307\u5b9a\u512a\u5148; \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af\u306f K-Z3 \u73fe\u5728\u6642\u523b\u5e2f 23\u6642\u53f0 n \u7a4d\u307f\u5897\u3057\u7d9a\u884c\u3001\u6b21 run ID \u306f run406 \u4f7f\u7528)\u3002")

# append evidence to END of K-Z3 single-line cell
lines[kz3_idx] = lines[kz3_idx] + ev

# insert iter-log entry as a new line right after header
lines.insert(ilog_idx + 1, iter_entry)

out = "\n".join(lines)
with open(PATH, "w", encoding="utf-8") as f:
    f.write(out)

print("done; total lines", len(lines))