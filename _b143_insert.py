#!/usr/bin/env python3
path="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
s=open(path).read()
lines=s.split("\n")

# ---- 1) append run336 evidence to K-Z3 line (idx 278) end ----
idx=278
line=lines[idx]
anchor="確定的。status 判定は rank に委ねる (rank 専門)。"
assert line.endswith(anchor), "L279 anchor mismatch: "+repr(line[-60:])
ev=(" bench 2026-09-07 (第143回, K-Z3 10時台 n-add run336A\u2013C \u2014 rank 第146回 NEXT\u300cK-Z3 current-band(現時刻帯 10時台) n-add\u3001次 run ID \u306f run336 \u4f7f\u7528\u300d\u306e run336 \u67a0\u3068\u3057\u3066\u5b9f\u65bd, "
"同測定法 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, Tokyo, 10:40:05\u201310:40:15 JST, \u5168 80/80 200, "
"\u6b63 endpoint search.kotobase.net/search?q=test, host load1 20.25 (production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916), "
"secret \u4e0d\u542b \u2014 curl \u306e\u307f): cold(>=0.5s) 2/0/0 per 20 = 2/60 (~3.3%) \u2014 run336A cold 2/20 (1.2171s/1.5636s \u6563\u767a\u30da\u30a2) p50 48.2ms / B cold 0/20 p50 42.7ms / C cold 0/20 p50 43.7ms, "
"control (kotobase.net/signup) cold 0/20 p50 42.0ms max 65.1ms \u5b8c\u5168\u9759\u7a4f\u3067 control \u5206\u96e2\u6210\u7acb\u3001cold \u7fa4 search \u5074\u306b\u5c40\u5728\u3002"
"run336A \u6563\u767a\u30da\u30a2\u306f B/C 0/20 + control 0/20 \u3067\u5373\u6d88\u5931\u3057\u300c\u5e2f\u5185 1 \u7a93\u5373\u6d88\u5931\u300d\u6563\u767a\u5358\u767a/\u30da\u30a2\u578b\u7d9a\u3005 (run335A/B \u5404\u5358\u767a\u306e\u76f4\u5f8c\u6e1b\u5f31, heavy run331A 9/20 \u578b\u306f run331A \u4ee5\u964d 6 \u30bb\u30c3\u30c8\u9023\u7d9a\u975e\u518d\u73fe\u3067 10\u6642\u53f0\u5e2f\u5185\u3067\u306f\u91cd\u307f\u518d\u73fe\u306a\u3057). "
"10\u6642\u53f0 (9/7) \u901a\u7b97 = falsify154-run332 (4/60) + bench141-run333 (5/60) + falsify155-run333-indep (1/60) + bench142-run334 (2/60) + falsify156-run335 (2/60) + \u672c tick run336 (2/60) = 16/360 (~4.4%) \u306e 6 \u30bb\u30c3\u30c8\u4e2d\u4f4d\u5e2f\u5bc4\u308a\u3001"
"run331A heavy 9/20 \u521d\u518d\u51fa\u73fe\u306e\u5f31\u5f8c\u7d9a\u306f\u6563\u767a\u5358\u767a/\u30da\u30a2\u3078\u6e1b\u5f31\u7d99\u7d9a (heavy >=6/20 \u306b\u306f\u81f3\u3089\u305a\u5e2f\u5185 1 \u7a93\u5373\u6d88\u5931\u3078\u53ce\u675f\u65b9\u5411). "
"host load 20 \u306e p50 (search 42\u201348ms, control 42.0ms) \u306f\u540c\u6c34\u6e96\u3067\u5206\u6790\u6cd5\u306b\u5f71\u97ff\u306a\u3057\u3001cold \u5224\u5b9a 2/60 \u306f control \u5b8c\u5168\u9759\u7a4f\u3067\u78ba\u5b9a\u7684\u3002status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002")
lines[idx]=line+ev

# ---- 2) insert bench 143 iteration-log entry below header (newest-first) ----
hdr=None
for i,l in enumerate(lines):
    if l.strip()=="## Iteration log":
        hdr=i; break
assert hdr is not None
entry=("- 2026-09-07: bench \u7b2c143\u56de\u300210:40 JST tick\u3002HEAD bd2018d = falsify \u7b2c156\u56de (10:32, K-Z3 10\u6642\u53f0 run335) = remote net-kotobase/main \u4e00\u81f4 "
"(fetch + rev-parse \u6bd4\u8f03, \u50e2\u96e2 0; worktree detached HEAD \u306e\u305f\u3081 git pull --ff-only \u4e0d\u53ef, fetch \u7cfb\u3067\u53d6\u308a\u8fbc\u307f)\u3002"
"live smoke 200 (/, /signup; pre-run \u8a08\u6e2c)\u3002host load1 19.03\u219220.25 (gate 7.5 \u5927\u5e45\u8d85\u904e) \u306e\u305f\u3081 local \u6e2c\u5b9a\u306f\u62d2\u5426\u3057 production HTTP \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af (gate \u5916)\u3002"
"\u203bpre-run monitor NEXT\u300cK-Z3 \u6df1\u591c\u5e2f 23\u6642\u53f0 n \u7a4d\u307f\u5897\u3057\u7d99\u7d9a\u300d\u306f stale (rank \u7b2c90\u56de\u5e2f artifact) \u2014 true progressive NEXT \u306f rank \u7b2c146\u56de (Iteration log \u672b\u5c3e)\u300cK-Z3 current-band(\u73fe\u6642\u523b\u5e2f 10\u6642\u53f0) n-add\u3001\u6b21 run ID \u306f run336 \u4f7f\u7528\u300d\u306e run336 \u67a0\u3092\u672c tick \u5b9f\u65bd\u3002"
"K-Z3 10\u6642\u53f0 run336A\u2013C \u3092\u5b9f\u6e2c (\u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, cold>=0.5s, nearest-rank p50, \u6b63 endpoint search.kotobase.net/search?q=test, 10:40:05\u201310:40:15 JST, \u5168 80/80 200): "
"A cold 2/20 (1.2171s/1.5636s \u6563\u767a\u30da\u30a2) p50 48.2ms / B cold 0/20 p50 42.7ms / C cold 0/20 p50 43.7ms / control (kotobase.net/signup) cold 0/20 p50 42.0ms max 65.1ms \u5b8c\u5168\u9759\u7a4f\u3067 control \u5206\u96e2\u6210\u7acb\u3001cold \u7fa4 search \u5074\u306b\u5c40\u5728 \u2014 "
"search cold 2/60 (~3.3%) \u6563\u767a\u5358\u767a/\u30da\u30a2\u578b\u300c\u5e2f\u5185 1 \u7a93\u5373\u6d88\u5931\u300d\u7d99\u7d9a\u3001run335A/B \u5404\u5358\u767a\u306e\u76f4\u5f8c\u6e1b\u5f31\u3001heavy run331A 9/20 \u578b\u306f 6 \u30bb\u30c3\u30c8\u9023\u7d9a\u975e\u518d\u73fe\u3002"
"10\u6642\u53f0 (9/7) \u901a\u7b97 = 14/300 (~4.7%, rank \u7b2c146\u56de fold) + \u672c tick 2/60 = 16/360 (~4.4%) \u306e 6 \u30bb\u30c3\u30c8\u4e2d\u4f4d\u5e2f\u5bc4\u308a\u3001heavy >=6/20 \u306b\u306f\u81f3\u3089\u305a\u5e2f\u5185 1 \u7a93\u5373\u6d88\u5931\u3078\u53ce\u675f\u65b9\u5411\u3002"
"status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002secret \u306f\u4e00\u5207\u8a18\u9332\u305b\u305a\u3002\u8a73\u7d30\u306f K-Z3 evidence \u6b04 (L279 \u672b\u5c3e\u8ffd\u8a18)\u3002"
"NEXT: \u59d4\u306d\u308b (rank \u6307\u5b9a\u512a\u5148; \u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af\u306f K-Z3 \u73fe\u5728\u6642\u523b\u5e2f n \u7a4d\u307f\u5897\u3057\u7d99\u7d9a\u3001\u6b21 run ID \u306f run337 \u4f7f\u7528)")
lines.insert(hdr+1, entry)

open(path,"w").write("\n".join(lines))
print("done. new L279 len:",len(lines[278]))
print("iterlog newest idx:",hdr+1,":",repr(lines[hdr+1][:60]))
print("total lines:",len(lines))