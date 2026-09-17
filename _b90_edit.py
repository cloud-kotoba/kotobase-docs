#!/usr/bin/env python3
MD="/Users/junkawasaki/github/com-junkawasaki/orgs/net-kotobase/docs/query-cosientist.md"
data=open(MD,encoding="utf-8").read()

# ---- evidence to append to K-Z3 row (after falsify 第89回 tail) ----
# actual text uses ASCII hyphen "13-15時帯連続" then filler
anchor="13-15\u6642\u5e2f\u9023\u7d9a\u3067\u4f4e\u4f4d\u5e2f\u7d9a\u304f\u3002status \u79fb\u884c\u306a\u3057 (rank \u5c02\u9580)\u3002secret \u306f\u4e00\u5207\u8a18\u9332\u305b\u305a (curl \u306e\u307f)\u3002"
print("anchor_count_a=", data.count(anchor[:20]))

ev = (
 " bench 2026-09-06 (\u7b2c89\u56de, K-Z3 15\u6642\u53f0 2\u30bb\u30c3\u30c8\u76ee run216A\u2013C, "
 "\u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, Tokyo, "
 "15:09:47\u201315:09:56 JST, \u5168 80/80 200, \u6b63 endpoint search.kotobase.net/search?q=test, "
 "host load1 77.81 (gate 7.5 \u8d85\u904e) \u306f production HTTP \u5b9f\u6e2c\u306e\u305f\u3081 gate \u5916): "
 "run216A cold(>=0.5s) 1/20 (0.911s 3\u756a\u76ee\u306e\u5358\u767a) p50 43.1ms / run216B cold 0/20 "
 "p50 47.0ms / run216C cold 0/20 p50 53.5ms \u2014 landing control (kotobase.net/signup, \u540c\u6642\u523b, "
 "n=20, \u5168 200) \u306f cold 0/20 p50 51.0ms max 249.0ms \u3068\u9759\u7a4f\u3067 control \u5206\u96e2\u6210\u7acb\u3001"
 "cold \u7fa4\u306f search \u5074\u306b\u5c40\u5728\u3002falsify \u7b2c89\u56de run215B/C \u306e\u540c\u6642\u4e0a\u632f\u308c\u306f"
 "\u975e\u518d\u73fe\u3067 run216A \u5358\u767a\u306e\u307f\u306e\u300c\u5e2f\u5185 1 \u7a93\u5373\u6d88\u5931\u300d\u30d1\u30bf\u30fc\u30f3\u3068\u6574\u5408\u3002"
 "15\u6642\u53f0\u901a\u7b97 run215 (2/60) + \u672c tick (1/60) = 3/120 (~2.5%) \u4f4e\u4f4d\u5e2f\u6b8b\u754c\u7d99\u7d9a\u3002"
 "status \u5224\u5b9a\u306f rank \u306b\u59d4\u306d\u308b (rank \u5c02\u9580)\u3002"
)
if data.count(anchor)==1:
    data=data.replace(anchor, anchor+ev, 1)
    print("EVIDENCE_APPENDED")
else:
    print("EVIDENCE_SKIP count=", data.count(anchor))

# ---- iteration log entry ----
hdr="## Iteration log\n"
print("hdr_count=", data.count(hdr))
entry=(
 "- 2026-09-06: bench \u7b2c89\u56de\u300215:09 JST tick\u3002worktree detached HEAD \u306e\u305f\u3081 "
 "fetch net-kotobase + rev-parse \u6bd4\u8f03\u3067\u53d6\u308a\u8fbc\u307f (HEAD \u306f rank \u7b2c88\u56de local commit 8255634, "
 "parent 067b109 = fetch \u5f8c net-kotobase/main \u5148\u7aef\u4e00\u81f4\u3001NEXT cacao_b64 harness / K-Z3 15\u6642\u53f0 \u3092\u78ba\u8a8d)\u3002"
 "live smoke 200 (/, /signup; pre-run \u8a08\u6e2c)\u3002host load1 77.81 (gate 7.5 \u8d85\u904e) \u306e\u305f\u3081 local \u6e2c\u5b9a\u306f\u62d2\u5426\u3057"
 "\u300chost busy (load1 77.81)\u300d\u3092\u8a18\u9332\u3002\u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af (production HTTP \u5b9f\u6e2c, gate \u5916): "
 "K-Z3 15\u6642\u53f0 2\u30bb\u30c3\u30c8\u76ee run216A\u2013C (\u540c\u6e2c\u5b9a\u6cd5 n=20 \u00d7 3 + landing control, \u5225\u63a5\u7d9a curl, "
 "15:09:47\u201315:09:56 JST, \u5168 80/80 200, \u6b63 endpoint search.kotobase.net/search?q=test): "
 "cold 1/0/0 per 20 = 1/60 (~1.7%) \u2014 run216A \u5358\u767a 0.911s (3\u756a\u76ee) \u306e\u307f, run216B/C 0/20 "
 "(p50 47.0/53.5ms), control (kotobase.net/signup) cold 0/20 p50 51.0ms max 249.0ms \u9759\u7a4f\u3067 "
 "control \u5206\u96e2\u6210\u7acb\u3001cold \u7fa4\u306f search \u5074\u306b\u5c40\u5728\u3002falsify \u7b2c89\u56de run215 (2/60) \u306e\u540c\u6642\u4e0a\u632f\u308c\u306f"
 "\u672c tick \u3067\u306f\u975e\u518d\u73fe (run216A \u5358\u767a 1/60) \u3067 run212A\u2192run213A \u578b\u300c\u5e2f\u5185 1 \u7a93\u5373\u6d88\u5931\u300d\u30d1\u30bf\u30fc\u30f3\u3068\u6574\u5408\u3002"
 "15\u6642\u53f0\u901a\u7b97 run215 + \u672c tick = 3/120 ~2.5% \u4f4e\u4f4d\u5e2f\u6b8b\u754c\u7d9a\u304f (14\u6642\u53f0 10/240 ~4.2% \u3068 13-15\u6642\u5e2f\u9023\u7d9a\u4f4e\u4f4d\u5e2f)\u3002"
 "status \u79fb\u884c\u306a\u3057 (rank \u5c02\u9580)\u3002secret \u306f\u4e00\u5207\u8a18\u9332\u305b\u305a (curl \u306e\u307f)\u3002NEXT: \u59d4\u306d\u308b (rank \u6307\u5b9a\u512a\u5148; "
 "\u30d5\u30a9\u30fc\u30eb\u30d0\u30c3\u30af\u306f K-Z3 \u73fe\u5728\u6642\u523b\u5e2f n \u7a4d\u307f\u5897\u3057\u7d99\u7d9a)\u3002\n"
)
if data.count(hdr)==1:
    data=data.replace(hdr, hdr+entry, 1)
    print("LOGGED")
else:
    print("LOG_SKIP")

open(MD,"w",encoding="utf-8").write(data)
print("DONE")